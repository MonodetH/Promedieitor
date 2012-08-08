# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregarEval.ui'
#
# Created: Wed Aug  8 02:56:48 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AgreEval(object):
    def setupUi(self, AgreEval):
        AgreEval.setObjectName(_fromUtf8("AgreEval"))
        AgreEval.resize(271, 101)
        self.label = QtGui.QLabel(AgreEval)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AgreEval)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.buttonBox = QtGui.QDialogButtonBox(AgreEval)
        self.buttonBox.setGeometry(QtCore.QRect(100, 70, 156, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(AgreEval)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.spinBox = QtGui.QDoubleSpinBox(AgreEval)
        self.spinBox.setGeometry(QtCore.QRect(181, 30, 71, 21))
        self.spinBox.setDecimals(1)
        self.spinBox.setMaximum(100.0)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.retranslateUi(AgreEval)
        QtCore.QMetaObject.connectSlotsByName(AgreEval)
        AgreEval.setTabOrder(self.lineEdit, self.spinBox)
        AgreEval.setTabOrder(self.spinBox, self.buttonBox)

    def retranslateUi(self, AgreEval):
        AgreEval.setWindowTitle(QtGui.QApplication.translate("AgreEval", "Agregar Evaluación", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AgreEval", "Nombre de evaluación", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AgreEval", "Nota", None, QtGui.QApplication.UnicodeUTF8))

