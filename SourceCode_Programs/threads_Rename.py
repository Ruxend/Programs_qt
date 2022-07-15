# -*- coding: utf-8 -*-
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import (QTextCursor,QColor,QPalette)
from PyQt5.QtCore import (QThread,pyqtSignal)
from random import randint
import asyncio,os,sys,time,xlrd,xlwt
from ui_Rename import ui_Rename

class WorkThread_Rename(QThread):
	# 使用信号和UI主线程通讯，参数是发送信号时附带参数的数据类型，可以是str、int、list等
	finishSignal = pyqtSignal(int)
	signal_1 = pyqtSignal(str, str)
	signal_2 = pyqtSignal(str)
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
		owb_fn = self.entry_1
		ows_tn = self.entry_2
		listpath = "{}/".format(self.entry_3)
		ext = ".{}".format(self.entry_4)
		owb = xlrd.open_workbook(owb_fn)
		ows = owb.sheet_by_name(ows_tn)
		# Getlist
		filelist = list(map(str, ows.col_values(0)[1:]))
		nfilelist = list(map(str, ows.col_values(1)[1:]))

		length = len(filelist)  		# 获取程序长度
		self.signal_len.emit(length)  	# 发射进度条最大值
		step = 0

		for ntrow in range(1, ows.nrows):
			if filelist[ntrow-1] != sys.argv[0] and filelist[ntrow-1] == str(ows.cell(ntrow, 0).value):
				if ext.split(".")[1].rstrip() != "":
					new_data = nfilelist[ntrow-1]+ext
					path_data = listpath+filelist[ntrow-1]+ext
				elif os.path.isdir(listpath+"/"+filelist[ntrow-1]):
					new_data = nfilelist[ntrow-1]
					path_data = listpath+filelist[ntrow-1]
				path_new_data = listpath+new_data
				if os.path.exists(path_data):
					os.rename(path_data, path_new_data) 		# 输出内容
					self.signal_1.emit(path_data, new_data)  	# 发射内容输出
				else:
					self.signal_2.emit(path_data)  				# 发射内容输出
			step += 1
			self.signal_step.emit(step)  		# 发射进度条实时进度
		self.finishSignal.emit(length)  		# 发射程序结束输出
		await asyncio.sleep(0)
		
		
# entry_1 = "D:/Dev/Object/Python/test/222.xls"
# entry_2 = "222"
# entry_3 = "D:/Dev/Object/Python/test1"
# entry_4 = "txt"
# WorkThread(entry_1=entry_1, entry_2=entry_2, entry_3=entry_3, entry_4=entry_4).run()