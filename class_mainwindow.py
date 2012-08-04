#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_mainwindow.py
#

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
import sys
from ui_mainwindow import Ui_MainWindow
from class_agregarEval import *
from class_agregarVar import *

# Se hereda de la clase QtGui.QMainWindow
class Principal(QtGui.QMainWindow):
	# Se define el constructor de la clase __init__
	def __init__(self):
		# Se llama al constructor de la clase padre
		QtGui.QMainWindow.__init__(self)
		# Se crea la instancia de Ui_MainWindow
		self.ventana = Ui_MainWindow()
		self.ventana.setupUi(self)
        
		self.ventana.pushButton.connect(self.ventana.pushButton, SIGNAL("clicked()"),self, SLOT("addEval()"))
		self.ventana.pushButton_2.connect(self.ventana.pushButton_2, SIGNAL("clicked()"),self, SLOT("addVar()"))
		
	@pyqtSlot()
	def addEval(self):
		self.popEval = PopEval()
		r = self.popEval.exec_()
		print r
		if r:
			print "Eval: " + self.popEval.ventana.lineEdit.text() + "\nNota: " + str(self.popEval.ventana.spinBox.value())
		
	@pyqtSlot()
	def addVar(self):
		self.popVar = PopVar()
		r = self.popVar.exec_()
		print r

