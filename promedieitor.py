#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  promedieitor.py
#  
#  Copyright 2012 MonodetH <monodeth@monodeth-NB>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from PyQt4 import QtCore, QtGui
import sys
from mainwindow import Ui_MainWindow
from agregarEval import Ui_Dialog

class popEval(QtGui.QMainWindow)
	def __init__(self):
		
	
# Se hereda de la clase QtGui.QMainWindow
class Principal(QtGui.QMainWindow):
	# Se define el constructor de la clase __init__
    def __init__(self):
        # Se llama al constructor de la clase padre
        QtGui.QMainWindow.__init__(self)
        # Se crea la instancia de Ui_MainWindow
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)

def main():
	app = QtGui.QApplication(sys.argv)
	principal = Principal()
	principal.show()
	sys.exit(app.exec_())
	return 0

if __name__ == '__main__':
	main()

