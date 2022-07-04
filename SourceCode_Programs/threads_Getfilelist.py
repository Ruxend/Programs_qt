#！/usr/bin/env python3
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import (QTextCursor,QColor,QPalette)
from PyQt5.QtCore import (QThread,pyqtSignal)
from random import randint
import asyncio,os,time,openpyxl,xlrd,xlwt
from eth import eth
from xlwt_style import style
from ui_Getfilelist import ui_Getfilelist

class WorkThread_Getfilelist(QThread):
	# 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
	finishSignal = pyqtSignal(int)
	signal_1 = pyqtSignal(str, str)
	signal_len = pyqtSignal(int)
	signal_step = pyqtSignal(int)
	def __init__(self, *args, **kwargs):
		super().__init__()
		self.entry_1 = kwargs["entry_1"]
		self.entry_2 = kwargs["entry_2"]
		self.entry_3 = kwargs["entry_3"]
		self.entry_4 = kwargs["entry_4"]
		self.entry_5 = kwargs["entry_5"]
		self.text = kwargs["text"]
		self.num = 500  	# 设置数量
		# self.run()

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
		nwb_fn = owb_fn = self.entry_1
		nws_tn = ows_tn = self.entry_2
		nfp = "{}/".format(self.entry_3)
		ofp = "{}/".format(self.entry_4)
		ext = ".{}".format(self.entry_5)
		nwb = xlwt.Workbook("utf-8")	# 创建Excel表并写入数据
		nws = nwb.add_sheet(nws_tn)	#在新对象中新建Sheet表
		filelists =  os.listdir(ofp)  # 获取ofilepath文件夹下的所有的文件
		# Getfilelist
		lst = []	
		for file in filelists:
			if ext.split(".")[1].rstrip() != "":
				if file.endswith(ext):
					lst.append(file)
			elif os.path.isdir(ofp+"/"+file):
				lst.append(file)
		lst = sorted(lst, key=eth.ethkey)  #排序
		
		length = len(lst)  				# 获取程序长度
		self.signal_len.emit(length)  	# 发射进度条最大值
		step = 0
		# Write to Excel
		title = ["_Oldname__", "_Newname__"]
		for ind in title:
			nws.write(0, title.index(ind), title[title.index(ind)], style=style)
		rnum = 1
		for ostr in lst:
			nws.write(rnum, 0, ostr.split(".")[0], style=style)  # 输出内容
			self.signal_1.emit(ofp, ostr)  			# 发射内容输出
			rnum += 1 
			step += 1 
			self.signal_step.emit(step) 		# 发射进度条实时进度
		nwb.save(nfp+nwb_fn+".xls")  			# 保存内容
		self.finishSignal.emit(length)  		# 发射程序结束输出
		await asyncio.sleep(0)


# entry_1 = "111"
# entry_2 = "111"
# entry_3 = "D:/Dev/Object/Python/test"
# entry_4 = "D:/Dev/Object/Python/test1"
# entry_5 = "txt"
# WorkThread_Getfilelist(entry_1=entry_1, entry_2=entry_2, entry_3=entry_3, entry_4=entry_4, entry_5=entry_5).run()

