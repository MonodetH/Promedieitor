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
from class_core import *

# Se hereda de la clase QtGui.QMainWindow
class Principal(QtGui.QMainWindow):
	# Se define el constructor de la clase __init__
	def __init__(self):
		# Se llama al constructor de la clase padre
		QtGui.QMainWindow.__init__(self)
		# Se crea la instancia de Ui_MainWindow
		self.ventana = Ui_MainWindow()
		self.ventana.setupUi(self)
        
		self.model1 = EvalTableModel([["EDITAME","0"]])
		self.ventana.tableView.setModel(self.model1)

		self.model2 = VarTableModel([["NF","0","SUMA","EDITAME","1.0"]])
		self.ventana.tableView_2.setModel(self.model2)

		self.ventana.pushButton.connect(self.ventana.pushButton, SIGNAL("clicked()"),self, SLOT("addEval()"))
		self.ventana.pushButton_2.connect(self.ventana.pushButton_2, SIGNAL("clicked()"),self, SLOT("addVar()"))
		self.ventana.pushButton_3.connect(self.ventana.pushButton_3, SIGNAL("clicked()"),self, SLOT("resetAll()"))
		self.ventana.pushButton_4.connect(self.ventana.pushButton_4, SIGNAL("clicked()"),self, SLOT("generarNF()"))
		
	def generar(self,nombre):
		row = self.model2.getVar(nombre)
		if row == 0:
			return self.model1.getNota(nombre)
		elif row[0] == "CONSTANTE":
			return self.model2.getNota(nombre)
		elif row[0] == "SUMA":
			param = [x.strip() for x in str(row[1]).split(',')]
			retorno = 0
			for x in param:
				if x[0] == '-':
					retorno -= self.generar(x[1:])
				else:
					retorno += self.generar(x)
			nota = float(row[2])*retorno
			ubica = self.model2.ubicaNombre(nombre)
			self.model2.setValor(ubica, nota)
			return nota
		elif row[0] == "PRODUCTO":
			param = [x.strip() for x in str(row[1]).split(',')]
			retorno = 1
			for x in param:
				if x[0] == '-':
					retorno = -retorno * self.generar(x[1:])
				else:
					retorno *= self.generar(x)
			nota = float(row[2])*retorno
			ubica = self.model2.ubicaNombre(nombre)
			self.model2.setValor(ubica, nota)
			return nota
		elif row[0] == "PROMEDIO":
			param = [x.strip() for x in str(row[1]).split(',')]
			retorno = 0
			for x in param:
				if x[0] == '-':
					retorno -= self.generar(x[1:])
				else:
					retorno += self.generar(x)
			nota = float(row[2])*retorno/float(len(param))
			ubica = self.model2.ubicaNombre(nombre)
			self.model2.setValor(ubica, nota)
			return nota
		"""
		elif row[0] == "CONDICIONAL":
			param = [x.strip() for x in str(row[1]).split(';')]
			for i in range(len(param)):
				param[i] = [x.strip() for x in str(param[i]).split(':')]
				param[i][0] = [x.strip() for x in str(param[i][0]).split(',')]
				for j in range(len(param[i][0])):
					param[i][0][j] = [x.strip() for x in str(param[i][0][j]).split(' ')]
			print param
		"""	
	
	
	@pyqtSlot()
	def addEval(self):
		self.popEval = PopEval()
		r = self.popEval.exec_()
		if r:
			self.model1.insertRow(self.model1.rowCount(),[self.popEval.ventana.lineEdit.text(),\
			str(self.popEval.ventana.spinBox.value())])
		
	@pyqtSlot()
	def addVar(self):
		self.popVar = PopVar()
		r = self.popVar.exec_()
		if r:
			ruta = self.popVar.ventana
			self.model2.insertRow(self.model2.rowCount(),[ruta.nomVar.text(),str(ruta.valorVar.value()),\
			ruta.comboBox.currentText(),ruta.parVar.toPlainText(),str(ruta.pondVar.value())])
		
	@pyqtSlot()
	def resetAll(self):
		self.model1 = EvalTableModel([["EDITAME","0"]])
		self.ventana.tableView.setModel(self.model1)
		
		self.model2 = VarTableModel([["NF","0","SUMA","EDITAME","1.0"]])
		self.ventana.tableView_2.setModel(self.model2)
		
	@pyqtSlot()
	def generarNF(self):
		self.generar("NF")
		self.ventana.tableView_2.setModel(self.model2)
	





		
