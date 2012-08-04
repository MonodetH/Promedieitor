#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  class_agregarEval.py
#

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, SLOT, pyqtSlot
import sys
from ui_agregarVar import Ui_AgreVar

# Se hereda de la clase QtGui.QDialog
class PopVar(QtGui.QDialog):
	# Se define el constructor de la clase __init__
    def __init__(self):
        # Se llama al constructor de la clase padre
        QtGui.QDialog.__init__(self)
        # Se crea la instancia de Ui_Dialog
        self.ventana = Ui_AgreVar()
        self.ventana.setupUi(self)

        self.ventana.buttonBox.connect(self.ventana.buttonBox, SIGNAL("accepted()"),self, SLOT("accept()"))
        self.ventana.buttonBox.connect(self.ventana.buttonBox, SIGNAL("rejected()"),self, SLOT("reject()"))
        self.ventana.comboBox.connect(self.ventana.comboBox,SIGNAL("currentIndexChanged(QString)"),self,SLOT("deshabil"))
        self.ventana.comboBox.currentIndexChanged[str].connect(self.deshabil)

    def deshabil(self):
        tipo=self.ventana.comboBox.currentText()
        print tipo
        if tipo == "BASE":
            self.ventana.parVar.setEnabled(0)
            self.ventana.pondVar.setEnabled(0)
            self.ventana.label_3.setEnabled(0)
            self.ventana.label_7.setEnabled(0)
        else:
            self.ventana.parVar.setEnabled(1)
            self.ventana.pondVar.setEnabled(1)
            self.ventana.label_3.setEnabled(1)
            self.ventana.label_7.setEnabled(1)