# -*- coding: utf-8 -*-
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import (QTextCursor,QColor,QPalette)
from PyQt5.QtCore import (QThread,pyqtSignal)
from random import randint
import asyncio,os,time,openpyxl,xlrd,xlwt
from ui_Makedirs import ui_Makedirs

class WorkThread_Makedirs(QThread):
	# 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
	finishSignal = pyqtSignal(int)
	signal_1 = pyqtSignal(str, str, str)
	signal_2 = pyqtSignal(str, str, str)
	signal_len = pyqtSignal(int)
	signal_step = pyqtSignal(int)
	def __init__(self, *args, **kwargs):
		super().__init__()
		self.entry_1 = kwargs["entry_1"]
		self.entry_2 = kwargs["entry_2"]
		self.entry_3 = kwargs["entry_3"]
		self.entry_4 = kwargs["entry_4"]
		self.text = kwargs["text"]
		self.num = 500  	# 设置数量
		
	def run(self):
		asyncio.run(self.Work())
		return

	def create_multiasync(self):
		self.coro = [asyncio.ensure_future(self.Work()) for i in range(self.num)] 	# 协程列表

	def action_multiasync(self):
		loop = asyncio.get_event_loop()
		try:
			loop.run_until_complete(asyncio.wait(self.coro))
		except KeyboardInterrupt as e:
			for task in asyncio.Task.all_tasks():
				task.cancel()
			loop.stop()
			loop.run_forever()
		finally:
			loop.close()
	
	async def Work(self):
		"""批量创建文件"""
		owb_fn = self.entry_1
		ows_tn = self.entry_2
		path = "{}/".format(self.entry_3)
		ext = ".{}".format(self.entry_4)
		owb = xlrd.open_workbook(owb_fn)
		ows = owb.sheet_by_name(ows_tn)
		# Getfilelist
		filelist = list(map(str, ows.col_values(0)[1:]))

		length = ows.nrows - 1  		# 获取程序长度
		self.signal_len.emit(length)  	# 发射进度条最大值
		step = 0

		for otrow in range(1, ows.nrows): 
			data = filelist[otrow-1]
			if not os.path.exists(path+data+ext):   #判断如果文件不存在,则创建
				if ext.split(".")[1].rstrip() == "":
					os.makedirs(path+data)
				elif ext.split(".")[1].rstrip() == "xls":
					nwb = xlwt.Workbook("utf-8")
					nws = nwb.add_sheet("Sheet0")
					nwb.save(path+data+ext)
				elif ext.split(".")[1].rstrip() == "xlsx":
					nwb = openpyxl.Workbook("utf-8")
					nws = nwb.create_sheet("Sheet0")
					nwb.save(path+data+ext)
				else:
					with open(path+data+ext, "a") as f:
						f.write("")
				self.signal_1.emit(path, data, ext)  		# 发射内容输出
			else:
				self.signal_2.emit(path, data, ext)  		# 发射内容输出
			
			step += 1
			self.signal_step.emit(step)  		# 发射进度条实时进度
		self.finishSignal.emit(length)  		# 发射程序结束输出
		await asyncio.sleep(0)

		
		
# entry_1 = "D:/Dev/Object/Python/test/333.xls"
# entry_2 = "333"
# entry_3 = "D:/Dev/Object/Python/test1"
# entry_4 = "txt"
# WorkThread_Makedirs(entry_1=entry_1, entry_2=entry_2, entry_3=entry_3, entry_4=entry_4).run()