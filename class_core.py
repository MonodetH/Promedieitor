#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_core.py
#

from PyQt4 import QtGui, QtCore, uic
from types import *
import sys

class EvalTableModel(QtCore.QAbstractTableModel):
	
	def __init__(self, datos = [[]], parent = None):
		QtCore.QAbstractTableModel.__init__(self, parent)
		self.__datos = datos
		self.__headers = ["Nombre", "Nota"]

	def rowCount(self, parent = None):
		return len(self.__datos)

	def columnCount(self, parent):
		return len(self.__datos[0])

	def flags(self, index):
		return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

	def data(self, index, role):
		if role == QtCore.Qt.EditRole:
			row = index.row()
			column = index.column()
			return self.__datos[row][column]

		if role == QtCore.Qt.DisplayRole:
			row = index.row()
			column = index.column()
			value = self.__datos[row][column]
			return value

	def setData(self, index, value, role = QtCore.Qt.EditRole):
		if role == QtCore.Qt.EditRole:
			row = index.row()
			column = index.column()
			color = value
			self.__datos[row][column] = color.toString()
			self.dataChanged.emit(index, index)
			return True
		return False

	def headerData(self, section, orientation, role):
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				if section < len(self.__headers):
					return self.__headers[section]
				else:
					return "not implemented"
			else:
				return QtCore.QString("Eval %1").arg(section+1)

	def getNota(self, nombre):
		for i in range(self.rowCount()):
			row = self.__datos[i]
			if row[0] == nombre:
				return float(row[1])
		return 0
	
	def printRow(self, row):
		return str(self.__datos[row][0]) + "|" + str(self.__datos[row][1])
		
	def printRowP(self, row):
		return str(self.__datos[row][0]) + "|0" 
	
	def getName(self, row):
		return str(self.__datos[row][0])


    #=====================================================#
    #INSERTING & REMOVING
    #=====================================================#
	def insertRow(self, position, values, parent = QtCore.QModelIndex()):
		self.beginInsertRows(parent, position, position)
		self.__datos.insert(position, values)
		self.endInsertRows()
		return True

	def removeRow(self, position, parent = QtCore.QModelIndex()):
		self.beginRemoveRows(parent, position, position)
		values = self.__datos[position]
		self.__datos.remove(values)
		self.endRemoveRows()
		return True

class VarTableModel(QtCore.QAbstractTableModel):
	
	def __init__(self, datos = [[]], parent = None):
		QtCore.QAbstractTableModel.__init__(self, parent)
		self.__datos = datos
		self.__headers = ["Nombre", "Valor", "Tipo", "Parametros", "Ponderacion"]

	def rowCount(self, parent = None):
		return len(self.__datos)

	def columnCount(self, parent):
		return len(self.__datos[0])

	def flags(self, index):
		if index.row() == 0 and index.column() == 0:
			return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
		elif index.column() == 1:
			return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
		return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

	def data(self, index, role):
		if role == QtCore.Qt.EditRole:
			row = index.row()
			column = index.column()
			return self.__datos[row][column]

		if role == QtCore.Qt.DisplayRole:
			row = index.row()
			column = index.column()
			value = self.__datos[row][column]
			return value

	def setData(self, index, value, role = QtCore.Qt.EditRole):
		if role == QtCore.Qt.EditRole:
			row = index.row()
			column = index.column()
			color = value
			self.__datos[row][column] = color.toString()
			self.dataChanged.emit(index, index)
			return True
		return False

	def setValor(self, row, value, role = QtCore.Qt.EditRole):
		if role == QtCore.Qt.EditRole:
			index = self.index(row,1)
			value = QtCore.QVariant(value)
			self.setData(index,value)
			return True
		return False
	
	def headerData(self, section, orientation, role):
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				if section < len(self.__headers):
					return self.__headers[section]
				else:
					return "not implemented"
			else:
				return QtCore.QString("Var %1").arg(section+1)
	
	def getVar(self, nombre):
		for i in range(self.rowCount()):
			row = self.__datos[i]
			if row[0] == nombre:
				return [row[2],row[3],row[4]]
		return 0
	
	def getNota(self, nombre):
		for i in range(self.rowCount()):
			row = self.__datos[i]
			if row[0] == nombre:
				return row[1]
		return 0
	
	def ubicaNombre(self, nombre):
		for i in range(self.rowCount()):
			row = self.__datos[i]
			if row[0] == nombre:
				return i
		return None
	
	def printRow(self, row):
		return str(self.__datos[row][0]) + "|0|" + str(self.__datos[row][2]) + "|" +\
		str(self.__datos[row][3]) + "|" + str(self.__datos[row][4])
		
	def getName(self, row):
		return str(self.__datos[row][0])
		
    #=====================================================#
    #INSERTING & REMOVING
    #=====================================================#
	def insertRow(self, position, values, parent = QtCore.QModelIndex()):
		self.beginInsertRows(parent, position, position)
		self.__datos.insert(position, values)
		self.endInsertRows()
		return True

	def removeRow(self, position, parent = QtCore.QModelIndex()):
		self.beginRemoveRows(parent, position, position)
		values = self.__datos[position]
		self.__datos.remove(values)
		self.endRemoveRows()
		return True
