#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  promedieitor.pyw
#

from PyQt4 import QtCore, QtGui
import sys
from class_mainwindow import *

def main():
	app = QtGui.QApplication(sys.argv)
	if sys.platform == "win32" or sys.platform == "cygwin":
		app.setStyle("Cleanlooks")
	sys.setrecursionlimit(5000)
	principal = Principal()
	principal.show()
        sys.exit(app.exec_())
	return 0

if __name__ == '__main__':
	main()

