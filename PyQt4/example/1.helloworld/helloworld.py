#!/usr/bin/env python
# coding=utf-8
import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)
button = QPushButton("HelloWorld")
button.show()
app.exec_()

