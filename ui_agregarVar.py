# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarVar.ui'
#
# Created: Wed Aug  8 04:51:21 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AgreVar(object):
    def setupUi(self, AgreVar):
        AgreVar.setObjectName(_fromUtf8("AgreVar"))
        AgreVar.resize(251, 280)
        self.buttonBox = QtGui.QDialogButtonBox(AgreVar)
        self.buttonBox.setGeometry(QtCore.QRect(90, 250, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(AgreVar)
        self.label.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.nomVar = QtGui.QLineEdit(AgreVar)
        self.nomVar.setGeometry(QtCore.QRect(10, 30, 231, 20))
        self.nomVar.setObjectName(_fromUtf8("nomVar"))
        self.pondVar = QtGui.QDoubleSpinBox(AgreVar)
        self.pondVar.setEnabled(True)
        self.pondVar.setGeometry(QtCore.QRect(130, 80, 111, 22))
        self.pondVar.setMinimum(0.0)
        self.pondVar.setProperty("value", 1.0)
        self.pondVar.setObjectName(_fromUtf8("pondVar"))
        self.label_3 = QtGui.QLabel(AgreVar)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(AgreVar)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(AgreVar)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 91, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox = QtGui.QComboBox(AgreVar)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 111, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.toolButton = QtGui.QToolButton(AgreVar)
        self.toolButton.setGeometry(QtCore.QRect(90, 110, 21, 16))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.parVar = QtGui.QPlainTextEdit(AgreVar)
        self.parVar.setGeometry(QtCore.QRect(10, 130, 231, 111))
        self.parVar.setObjectName(_fromUtf8("parVar"))

        self.retranslateUi(AgreVar)
        QtCore.QMetaObject.connectSlotsByName(AgreVar)
        AgreVar.setTabOrder(self.nomVar, self.comboBox)
        AgreVar.setTabOrder(self.comboBox, self.pondVar)
        AgreVar.setTabOrder(self.pondVar, self.parVar)
        AgreVar.setTabOrder(self.parVar, self.buttonBox)
        AgreVar.setTabOrder(self.buttonBox, self.toolButton)

    def retranslateUi(self, AgreVar):
        AgreVar.setWindowTitle(QtGui.QApplication.translate("AgreVar", "Agregar Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AgreVar", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AgreVar", "Ponderacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AgreVar", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AgreVar", "Parámetros", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("AgreVar", "ALGEBRAICA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("AgreVar", "PROMEDIO", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("AgreVar", "CONDICIONAL", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setToolTip(QtGui.QApplication.translate("AgreVar", "<html><head/><body><p style=\'width: 300px;\' >Se recomienda fervientemente Revisar la seccion de Tipos de Variable que se encuentra en Ayuda->Variables->Tipos<br>O simplemente haciendo click en este boton</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("AgreVar", "?", None, QtGui.QApplication.UnicodeUTF8))

