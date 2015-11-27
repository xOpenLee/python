#!/usr/bin/env python
# coding=utf-8
import sys
from PyQt4 import QtGui, QtCore

class DemoWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300,300,200,200)
        self.setWindowTitle('Demo Window')
        quitBtn = QtGui.QPushButton('close',self)
        quitBtn.setGeometry(10,10,70,40)
        self.connect(quitBtn,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))

app = QtGui.QApplication(sys.argv)
dw = DemoWindow()
dw.show()
sys.exit(app.exec_())

