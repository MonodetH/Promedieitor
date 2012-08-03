#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  promedieitor.py
#

from PyQt4 import QtCore, QtGui
import sys
from class_mainwindow import *

def main():
	app = QtGui.QApplication(sys.argv)
	principal = Principal()
	principal.show()
        sys.exit(app.exec_())
	return 0

if __name__ == '__main__':
	main()

