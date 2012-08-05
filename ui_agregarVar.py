# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarVar.ui'
#
# Created: Sun Aug  5 00:16:06 2012
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
        self.parVar = QtGui.QTextEdit(AgreVar)
        self.parVar.setEnabled(True)
        self.parVar.setGeometry(QtCore.QRect(10, 130, 231, 101))
        self.parVar.setObjectName(_fromUtf8("parVar"))
        self.buttonBox = QtGui.QDialogButtonBox(AgreVar)
        self.buttonBox.setGeometry(QtCore.QRect(90, 250, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(AgreVar)
        self.label.setGeometry(QtCore.QRect(130, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.nomVar = QtGui.QLineEdit(AgreVar)
        self.nomVar.setGeometry(QtCore.QRect(10, 30, 111, 20))
        self.nomVar.setObjectName(_fromUtf8("nomVar"))
        self.valorVar = QtGui.QSpinBox(AgreVar)
        self.valorVar.setEnabled(False)
        self.valorVar.setGeometry(QtCore.QRect(130, 80, 101, 22))
        self.valorVar.setObjectName(_fromUtf8("valorVar"))
        self.pondVar = QtGui.QDoubleSpinBox(AgreVar)
        self.pondVar.setEnabled(True)
        self.pondVar.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.pondVar.setMinimum(0.0)
        self.pondVar.setObjectName(_fromUtf8("pondVar"))
        self.label_3 = QtGui.QLabel(AgreVar)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AgreVar)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(130, 60, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AgreVar)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(AgreVar)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 91, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox = QtGui.QComboBox(AgreVar)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 101, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.toolButton = QtGui.QToolButton(AgreVar)
        self.toolButton.setGeometry(QtCore.QRect(90, 110, 21, 16))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        self.retranslateUi(AgreVar)
        QtCore.QMetaObject.connectSlotsByName(AgreVar)

    def retranslateUi(self, AgreVar):
        AgreVar.setWindowTitle(QtGui.QApplication.translate("AgreVar", "Agregar Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AgreVar", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AgreVar", "Ponderacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AgreVar", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AgreVar", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AgreVar", "Parámetros", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("AgreVar", "SUMA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("AgreVar", "PRODUCTO", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("AgreVar", "PROMEDIO", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("AgreVar", "CONSTANTE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("AgreVar", "CONDICIONAL", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setToolTip(QtGui.QApplication.translate("AgreVar", "<html><head/><body><p>No olvidar EDITAR</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("AgreVar", "?", None, QtGui.QApplication.UnicodeUTF8))

