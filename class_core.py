from PyQt4 import QtGui, QtCore, uic
import sys

class TableModel(QtCore.QAbstractTableModel):
	
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
			self.__datos[row][column] = color
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



    #=====================================================#
    #INSERTING & REMOVING
    #=====================================================#
	def insertRow(self, position, nombre, nota, parent = QtCore.QModelIndex()):
		self.beginInsertRows(parent, position, position)
		values = [nombre,nota]
		self.__datos.insert(position, values)
		self.endInsertRows()
		return True

	def removeRow(self, position, parent = QtCore.QModelIndex()):
		self.beginRemoveRows(parent, position, position)
		values = self.__datos[position]
		self.__datos.remove(values)
		self.endRemoveRows()
		return True
