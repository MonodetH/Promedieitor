#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_mainwindow.py
#

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
import sys, re
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
		
		self.version = "0.5.0"
		self.name = "Promedieitor"
		
		ui = self.ventana
		ui.setupUi(self)
        
		self.model1 = EvalTableModel([["EDITAME","0"]])
		ui.tableView.setModel(self.model1)

		self.model2 = VarTableModel([["NF","0","ALGEBRAICA","EDITAME","1.0"]])
		ui.tableView_2.setModel(self.model2)

		ui.pushButton.connect(ui.pushButton, SIGNAL("clicked()"),self, SLOT("addEval()"))
		ui.pushButton_2.connect(ui.pushButton_2, SIGNAL("clicked()"),self, SLOT("addVar()"))
		ui.pushButton_3.connect(ui.pushButton_3, SIGNAL("clicked()"),self, SLOT("resetAll()"))
		ui.pushButton_4.connect(ui.pushButton_4, SIGNAL("clicked()"),self, SLOT("generarNF()"))
		ui.actionCargar.connect(ui.actionCargar, SIGNAL("triggered()"),self, SLOT("cargar()"))
		ui.actionGuardar.connect(ui.actionGuardar, SIGNAL("triggered()"),self, SLOT("guardar()"))
		ui.actionGuardar_plantilla.connect(ui.actionGuardar_plantilla, SIGNAL("triggered()"),self, SLOT("guardarPlantilla()"))
		
	def generar(self,nombre):
		row = self.model2.getVar(nombre)
		if row == 0:
			if re.match("[0-9]", nombre):
				return float(nombre)
			else:
				return self.model1.getNota(nombre)
		elif row[0] == "ALGEBRAICA":
			flag = False
			if row[1][0] == '-':
				row[1] = row[1][1:]
				flag = True
			param = [x.strip() for x in str(row[1]).split('-')]
			for i in range(len(param)):
				param[i] = [x.strip() for x in str(param[i]).split('+')]
				for j in range(len(param[i])):
					param[i][j] = [x.strip() for x in str(param[i][j]).split('/')]
					for k in range(len(param[i][j])):
						param[i][j][k] = [x.strip() for x in str(param[i][j][k]).split('*')]
			retorno = 0
			for i in range(len(param)):
				aux1 = 0
				for j in range(len(param[i])):
					aux2 = 1
					for k in range(len(param[i][j])):
						aux3 = 1
						for n in range(len(param[i][j][k])):
							aux3 *= self.generar(param[i][j][k][n])
						if k == 0:
							aux2 *= aux3
						else:
							aux2 /= aux3
					aux1 += aux2
				if i == 0:
					if flag:
						retorno -= aux1
					else:	
						retorno += aux1
				else:
					retorno -= aux1
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
			
		elif row[0] == "CONDICIONAL":
			param = [x.strip() for x in str(row[1]).split(';')]
			cond = [x.strip() for x in str(param[0]).split(',')]
			defecto = 0
			if len(param) == 2:
				defecto = self.generar(param[1])
			var = self.generar(cond[0])
			cond = cond[1:]
			
			for i in range(len(cond)):
				cond[i] = [x.strip() for x in str(cond[i]).split(':')]
				cond[i][0] = [x.strip() for x in str(cond[i][0]).split('&')]
				for j in range(len(cond[i][0])):
					cond[i][0][j] = [x.strip() for x in str(cond[i][0][j]).split(' ')]
			
			for i in range(len(cond)):
				flag = len(cond[i][0])
				for j in range(len(cond[i][0])):
					if cond[i][0][j][0] == '>':
						if var > self.generar(cond[i][0][j][1]):
							flag -= 1
							if flag == 0:
								retorno = self.generar(cond[i][1])
								nota = float(row[2])*retorno
								ubica = self.model2.ubicaNombre(nombre)
								self.model2.setValor(ubica, nota)
								return nota
					elif cond[i][0][j][0] == '>=':
						if var >= self.generar(cond[i][0][j][1]):
							flag -= 1
							if flag == 0:
								retorno = self.generar(cond[i][1])
								nota = float(row[2])*retorno
								ubica = self.model2.ubicaNombre(nombre)
								self.model2.setValor(ubica, nota)
								return nota
					elif cond[i][0][j][0] == '<':
						if var < self.generar(cond[i][0][j][1]):
							flag -= 1
							if flag == 0:
								retorno = self.generar(cond[i][1])
								nota = float(row[2])*retorno
								ubica = self.model2.ubicaNombre(nombre)
								self.model2.setValor(ubica, nota)
								return nota
					elif cond[i][0][j][0] == '<=':
						if var <= self.generar(cond[i][0][j][1]):
							flag -= 1
							if flag == 0:
								retorno = self.generar(cond[i][1])
								nota = float(row[2])*retorno
								ubica = self.model2.ubicaNombre(nombre)
								self.model2.setValor(ubica, nota)
								return nota
					elif cond[i][0][j][0] == '=' or cond[i][0][0][0] == '==':
						if var == self.generar(cond[i][0][j][1]):
							flag -= 1
							if flag == 0:
								retorno = self.generar(cond[i][1])
								nota = float(row[2])*retorno
								ubica = self.model2.ubicaNombre(nombre)
								self.model2.setValor(ubica, nota)
								return nota
					elif cond[i][0][j][0] == '!=':
						if var != self.generar(cond[i][0][j][1]):
							flag -= 1
							if flag == 0:
								retorno = self.generar(cond[i][1])
								nota = float(row[2])*retorno
								ubica = self.model2.ubicaNombre(nombre)
								self.model2.setValor(ubica, nota)
								return nota
			
			nota = float(row[2])*defecto
			ubica = self.model2.ubicaNombre(nombre)
			self.model2.setValor(ubica, nota)
			return nota
		else:
			nota = 0
			ubica = self.model2.ubicaNombre(nombre)
			self.model2.setValor(ubica, nota)
			return nota
	
	@pyqtSlot()
	def cargar(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', 'Archivo.ptf','Promedieitor Template (*.ptf);; All Files (*.*)')
		if str(filename) == '':
			pass
		else:
			f = open(filename, 'rbU')
			header = f.readline()
			header = [x.strip() for x in header.split(' ')]
			if header[1] != self.name:
				return False
			if header[2][:2] == "0.":
				data = f.readline()
				data = [x.strip() for x in data.split('&')]
				data = data[:len(data)-1]				
				for i in range(len(data)):
					data[i] = [x.strip() for x in data[i].split('|')]
				self.model1 = EvalTableModel(data)
				self.ventana.tableView.setModel(self.model1)
				
				data = f.readline()
				data = [x.strip() for x in data.split('&')]
				data = data[:len(data)-1]				
				for i in range(len(data)):
					data[i] = [x.strip() for x in data[i].split('|')]
				self.model2 = VarTableModel(data)
				self.ventana.tableView_2.setModel(self.model2)
						
			
	
	@pyqtSlot()
	def guardar(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', 'Archivo.ptf','Promedieitor Template (*.ptf);; All Files (*.*)')
		if str(filename) == '':
			pass
		else:
			f = open(filename, 'wb')
			f.write("<!# " + self.name + " " + self.version + " #!>\n")
			for i in range(self.model1.rowCount()):
				f.write(self.model1.printRow(i)+"&")
			f.write("\n")
			for i in range(self.model2.rowCount()):
				f.write(self.model2.printRow(i)+"&")
			f.close() 
	
	@pyqtSlot()
	def guardarPlantilla(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', 'Plantilla.ptf','Promedieitor Template (*.ptf);; All Files(*.*)')
		if str(filename) == '':
			pass
		else:
			f = open(filename, 'wb')
			f.write("<!# " + self.name + " " + self.version + " #!>\n")
			for i in range(self.model1.rowCount()):
				f.write(self.model1.printRowP(i)+"&")
			f.write("\n")
			for i in range(self.model2.rowCount()):
				f.write(self.model2.printRow(i)+"&")
			f.close() 
	
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
			self.model2.insertRow(self.model2.rowCount(),[ruta.nomVar.text(),"0",\
			ruta.comboBox.currentText(),ruta.parVar.toPlainText(),str(ruta.pondVar.value())])
		
	@pyqtSlot()
	def resetAll(self):
		self.model1 = EvalTableModel([["EDITAME","0"]])
		self.ventana.tableView.setModel(self.model1)
		
		self.model2 = VarTableModel([["NF","0","ALGEBRAICA","EDITAME","1.0"]])
		self.ventana.tableView_2.setModel(self.model2)
		
	@pyqtSlot()
	def generarNF(self):
		self.generar("NF")
		self.ventana.tableView_2.setModel(self.model2)
	
