#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_mainwindow.py
#

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT
import sys
from ui_mainwindow import Ui_MainWindow
from class_agregarEval import *

# Se hereda de la clase QtGui.QMainWindow
class Principal(QtGui.QMainWindow):
	# Se define el constructor de la clase __init__
    def __init__(self):
        # Se llama al constructor de la clase padre
        QtGui.QMainWindow.__init__(self)
        # Se crea la instancia de Ui_MainWindow
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.popEval = PopEval()
        self.ventana.pushButton.connect(self.ventana.pushButton, SIGNAL("clicked()"),self.popEval, SLOT("show()"))
    
    
