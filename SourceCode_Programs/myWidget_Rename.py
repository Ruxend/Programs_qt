# -*- coding: utf-8 -*-
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import (QApplication,QMainWindow,QDockWidget,QWidget,QFrame,QLabel,
						QLineEdit,QTextEdit,QPushButton,QDialog,QSlider,QMessageBox,
						QInputDialog,QFileDialog,QFontDialog,QColorDialog,QToolBar,
						QMenuBar,QStatusBar,QGroupBox,QGridLayout,QHBoxLayout,QVBoxLayout,
						QFormLayout,QListWidget,QScrollBar,QDesktopWidget,QProgressBar,
						QShortcut)
from PyQt5.QtGui import (QFont,QIcon,QPixmap,QColor,QTextCursor,QPalette,QKeySequence)
from PyQt5.QtCore import (Qt,QFile,QTimer,QDateTime,QThread,pyqtSignal,QBasicTimer,QObject)
# from PyQt5.QtMultimedia import QAudioInput,QAudioOutput,QAudioDeviceInfo
import os,sys,xlrd,xlwt,time
from random import randint
# from eth import eth
# from xlwt_style import style
from ui_Rename import ui_Rename
from threads_Rename import WorkThread_Rename

class myWidget_Rename(QMainWindow, ui_Rename):
	signal_child_2 = pyqtSignal()
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.btn_confirm.clicked.connect(self.Rename_confirm) 	# 连接槽
		QShortcut(QKeySequence("Return"), self, self.Rename_confirm)
		self.btn_quit.clicked.connect(self.close)				# 连接槽
		QShortcut(QKeySequence("Escape"), self, self.close)

	def get_entry_1(self):
		filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "Excel Files (*.xls;*.xlsx);;ALL Files(*.*)")
		self.entry_1.setText(filename)

	def get_entry_3(self):
		dire = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
		self.entry_3.setText(dire)

	def Rename_confirm(self):
		self.entry_1_value = self.entry_1.text()
		self.entry_2_value = self.entry_2.text()
		self.entry_3_value = self.entry_3.text()
		self.entry_4_value = self.entry_4.text()
		if self.entry_1_value=="" or self.entry_2_value=="" or self.entry_3_value=="": 
			self.text.append("----------Oops！Please Input All Necessary Parameters！----------\n")
			self.refresh_color()
			self.statusbar.showMessage("请输入必要参数!", 1000)
		else:
			try:
				self.work_start()
			except Exception as e:
				self.text.append("{}\n".format(e))  # 打印输出内容
				self.refresh_color()

	# def Rename_quit(self):
	# 	quit = QMessageBox.question(self, "Quit", "Do you want to quit ?", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
	# 	if quit == QMessageBox.Ok:
	# 		self.close()
	
	def work_start(self):
		self.btn_confirm.setDisabled(True)  	# 设置按钮不可用
		self.btn_confirm.setText("Waiting...")
		self.text.append("------------The program is running!------------\n")
		self.statusbar.showMessage("请稍等,正在处理...", 3600000)
		self.thread = WorkThread_Rename(entry_1=self.entry_1_value, entry_2=self.entry_2_value, 
								entry_3=self.entry_3_value, entry_4=self.entry_4_value, 
								text=self.text)
		# 将线程th的信号finishSignal和UI主线程中的槽函数button_finish进行连接
		self.thread.finishSignal.connect(self.work_finish)
		self.thread.signal_1.connect(self.signal_1_call)
		self.thread.signal_2.connect(self.signal_2_call)
		self.thread.signal_len.connect(self.call_progressbar)
		self.thread.signal_step.connect(self.progressbar_flush)
		self.thread.start()  				# 启动线程

	def signal_1_call(self, path_data, new_data):
		self.text.update()
		self.text.append("Put <{}>  rename <{}> successfully!".format(path_data, new_data))  # 打印输出内容
		self.refresh_color()

	def signal_2_call(self, path_data):
		self.text.update()
		self.text.append("Object <{}> does not exist!".format(path_data))  # 打印输出内容
		self.refresh_color()

	def work_finish(self, length):
		self.progressbar.hide()
		self.basictimer.stop()
		self.step = 0
		self.btn_confirm.setDisabled(False) 		# 设置按钮可用
		self.btn_confirm.setText("Confirm(&C)")
		self.text.update()
		self.text.append("\n----------Done! Data Output Successfully!----------\n")
		self.refresh_color()
		self.statusbar.showMessage(f"全部{str(length)}项,处理完成!", 3600000)
		done = QMessageBox.information(self, "Prompt!", "Done! Data Output Successfully!", QMessageBox.Ok, QMessageBox.Ok)
		if done == QMessageBox.Ok:
			self.statusbar.showMessage("")
		
	def refresh_color(self):
		self.text.moveCursor(QTextCursor.End)	   # 使滚动条位置一直处于最后
		self.text.setTextColor(QColor(randint(0,255),randint(0,255),randint(0,255),255)) # 改变text字体颜色
		self.text.update()
	
	# 每一个QObject对象或其子对象都有一个QObject.timerEvent方法
	# 为了响应定时器的超时事件，需要重写进度条的timerEvent方法
	def call_progressbar(self, length):
		self.maxstep = length
		self.progressbar.setMaximum(length)  	# 设定step最大值等效于.setRange(0, max)
		self.basictimer.start(10, self)  	# Param 1：超时时间；Param 2：超时后，接收定时器触发超时事件的对象。
		self.progressbar.show()

	def progressbar_flush(self, step):
		if step >= self.maxstep:
			self.progressbar.hide()
			self.basictimer.stop()
			self.step = 0
		self.progressbar.setValue(step)  			# 刷新进度

	def closeEvent(self, event):
		"""重写该方法使用sys.exit(0) 时就会只要关闭了主窗口，所有关联的子窗口也会全部关闭"""
		reply = QMessageBox.question(self, "Quit", "Do you want to quit ?", QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
			self.signal_child_2.emit()
		else:
			event.ignore()

	def keyPressEvent(self, e):
		"""绑定快捷键"""
		if e.key() == Qt._Key_Return:
			self.Rename_confirm()
		elif e.key() == Qt.Key_Escape:
			self.close()
	
# if __name__ == "__main__":
# 	app = QApplication(sys.argv)
# 	window = myWidget_Rename()
# 	window.show()
# 	sys.exit(app.exec())
	