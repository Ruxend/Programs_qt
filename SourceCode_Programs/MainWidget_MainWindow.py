#！/usr/bin/env python3
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import (QApplication,QMainWindow,QDockWidget,QWidget,QFrame,QLabel,
						QLineEdit,QTextEdit,QPushButton,QDialog,QSlider,QMessageBox,
						QInputDialog,QFileDialog,QFontDialog,QColorDialog,QToolBar,QSplashScreen,
						QMenuBar,QStatusBar,QGroupBox,QGridLayout,QHBoxLayout,QVBoxLayout,
						QFormLayout,QListWidget,QScrollBar,QDesktopWidget,QProgressBar,
						QShortcut)
from PyQt5.QtGui import (QFont,QIcon,QPixmap,QMovie,QColor,QTextCursor,QPalette,QKeySequence)
from PyQt5.QtCore import (Qt,QFile,QTimer,QDateTime,QThread,pyqtSignal,QBasicTimer,QElapsedTimer,
						QObject,QSize,QEventLoop)
from res import res
from ui_MainWindow import ui_MainWindow
from myWidget_Makedirs import myWidget_Makedirs
from myWidget_Getfilelist import myWidget_Getfilelist
from myWidget_Rename import myWidget_Rename
from loading import loadingSplash
from multiprocessing import Pool
import sys,asyncio

class main_MainWindow(QMainWindow, ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.btn_1.clicked.connect(self.show_child_1)   	# 连接槽
		self.btn_2.clicked.connect(self.show_child_2)   	# 连接槽
		self.btn_3.clicked.connect(self.show_child_3)   	# 连接槽
		self.btn_4.clicked.connect(self.show_child_4)   	# 连接槽
		self.btn_quit.clicked.connect(self.close)   		# 连接槽
		QShortcut(QKeySequence("Escape"), self, self.close)

	def show_child_1(self):
		self.child_1 = myWidget_Getfilelist()
		self.child_1.setWindowModality(Qt.ApplicationModal)
		self.child_1.signal_child_1.connect(self.show_MainWindow)
		self.child_1.show()
		self.hide()

	def show_child_2(self):
		self.child_2 = myWidget_Rename()
		self.child_2.setWindowModality(Qt.ApplicationModal)
		self.child_2.signal_child_2.connect(self.show_MainWindow)
		self.child_2.show()
		self.hide()

	def show_child_3(self):
		self.child_3 = myWidget_Makedirs()
		self.child_3.setWindowModality(Qt.ApplicationModal)
		self.child_3.signal_child_3.connect(self.show_MainWindow)
		self.child_3.show()
		self.hide()

	def show_child_4(self):
		msg = QMessageBox.information(self, "Prompt", "暂无更多, 敬请期待!", QMessageBox.Ok, QMessageBox.Ok)
		if msg == QMessageBox.Ok:
			self.statusbar.showMessage("")
		# self.child_4.show()
	
	def show_MainWindow(self):
		self.show()

	# def Main_quit(self):
	# 	quit = QMessageBox.question(self, "Quit", "Do you want to quit ?", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
	# 	if quit == QMessageBox.Ok:
	# 		self.close()

	def closeEvent(self, event):
		"""重写该方法使用sys.exit(0) 时就会只要关闭了主窗口，所有关联的子窗口也会全部关闭"""
		reply = QMessageBox.question(self, "Quit", "Do you want to quit ?", QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def keyPressEvent(self, e):
		"""绑定快捷键"""
		if e.key() == Qt._Key_1:
			self.show_child_1()
		elif e.key() == Qt._Key_2:
			self.show_child_2()
		elif e.key() == Qt._Key_3:
			self.show_child_3()
		elif e.key() == Qt._Key_3:
			self.show_child_3()
		elif e.key() == Qt.Key_Escape:
			self.close()

	# def mousePressEvent(self, event):
	# 	if event.button() == Qt.LeftButton:
	# 		self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
	# 		event.accept()
	# 	if event.button() == Qt.RightButton:
	# 		self.close()

	# def mouseMoveEvent(self, event):
	# 	if event.buttons() & Qt.LeftButton:
	# 		self.move(event.globalPos()-self.dragPosition)
	# 		event.accept()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	loading = loadingSplash(res.path("res\\day5.gif")) 			# 加载画面图片
	loading.showMessage("Loading......", Qt.AlignRight | Qt.AlignBottom)
	loading.setFont(QFont("微软雅黑", 12, QFont.Normal))
	loading.effect()  							# 调用加载效果
	loading.show()
	app.processEvents()  						# 设置启动画面不影响其他效果
	# pixmap = QPixmap("res\\loading.gif")
	# loading = QSplashScreen(pixmap)
	# # loading.resize(660, 520)					# 加载画面大小
	# screen = QDesktopWidget().screenGeometry()
	# size = loading.geometry()
	# loading.move(int((screen.width()-size.width())/2), int((screen.height()-size.height())/2) ) # 窗体居中显示   
	# label = QLabel(loading)
	# movie = QMovie("res\\loading.gif")
	# # movie.setScaledSize(QSize(660, 520))						# 自定义拉伸图片大小
	# label.setMovie(movie)
	# movie.start()
	# loading.show()
	# delayTime = 3.4
	# timer = QElapsedTimer()
	# timer.start()
	# while timer.elapsed() < (delayTime*1000):
	# 	app.processEvents()  						# 设置启动画面不影响其他效果
	window = main_MainWindow()
	window.show()
	loading.finish(window)							# 启动画面完成启动
	sys.exit(app.exec())
