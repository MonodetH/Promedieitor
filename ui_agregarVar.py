# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarVar.ui'
#
# Created: Fri Aug  3 22:07:54 2012
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
        AgreVar.resize(261, 390)
        self.textEdit_4 = QtGui.QTextEdit(AgreVar)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 240, 231, 101))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.buttonBox = QtGui.QDialogButtonBox(AgreVar)
        self.buttonBox.setGeometry(QtCore.QRect(90, 360, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.radioButton_2 = QtGui.QRadioButton(AgreVar)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 100, 101, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton = QtGui.QRadioButton(AgreVar)
        self.radioButton.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_4 = QtGui.QRadioButton(AgreVar)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 140, 101, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_3 = QtGui.QRadioButton(AgreVar)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 120, 101, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.label = QtGui.QLabel(AgreVar)
        self.label.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(AgreVar)
        self.comboBox.setGeometry(QtCore.QRect(138, 30, 111, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEdit = QtGui.QLineEdit(AgreVar)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox = QtGui.QSpinBox(AgreVar)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(130, 190, 51, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(AgreVar)
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setGeometry(QtCore.QRect(10, 190, 91, 22))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_3 = QtGui.QLabel(AgreVar)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(AgreVar)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(130, 170, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(AgreVar)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(AgreVar)
        self.label_6.setGeometry(QtCore.QRect(140, 10, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(AgreVar)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 220, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(AgreVar)
        QtCore.QMetaObject.connectSlotsByName(AgreVar)

    def retranslateUi(self, AgreVar):
        AgreVar.setWindowTitle(QtGui.QApplication.translate("AgreVar", "Agregar Variable", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("AgreVar", "Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("AgreVar", "Base", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_4.setText(QtGui.QApplication.translate("AgreVar", "Condición", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_3.setText(QtGui.QApplication.translate("AgreVar", "Promedio", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AgreVar", "Tipo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AgreVar", "Ponderacion", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AgreVar", "Valor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AgreVar", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AgreVar", "Padre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AgreVar", "Condición", None, QtGui.QApplication.UnicodeUTF8))

