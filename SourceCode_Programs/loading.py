#！/usr/bin/env python3
#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import (QApplication,QMainWindow,QFrame,QSplashScreen,QLabel,
							QDesktopWidget,QGridLayout)
from PyQt5.QtGui import QPixmap,QMovie,QIcon,QFont
from PyQt5.QtCore import Qt,QElapsedTimer,QSize
from res import res
import sys,time

class loadingSplash(QSplashScreen):
	def __init__(self, pathPixmap):
		super().__init__(QPixmap(pathPixmap))
		# self.loading = QSplashScreen(QPixmap(pathPixmap))

	def effect(self):
		self.setWindowOpacity(0)
		t = 0
		while t <= 1000:
			newOpacity = self.windowOpacity() + 0.02	# 设置淡入
			if newOpacity > 1:
				break
			self.setWindowOpacity(newOpacity)
			self.show()
			t -= 1
			time.sleep(0.02)
		time.sleep(1)				   					# 停留时间
		
		t = 0
		while t <= 1000:
			newOpacity = self.windowOpacity() - 0.02	# 设置淡出
			if newOpacity < 0:
				break
			self.setWindowOpacity(newOpacity)
			t += 1
			time.sleep(0.02)


