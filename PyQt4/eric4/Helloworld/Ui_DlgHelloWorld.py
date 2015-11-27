# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/xopenlee/git/python/PyQt4/eric4/Helloworld/DlgHelloWorld.ui'
#
# Created: Wed Aug 19 20:47:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(241, 171)
        self.lblHello = QtGui.QLabel(Dialog)
        self.lblHello.setGeometry(QtCore.QRect(100, 20, 66, 17))
        self.lblHello.setObjectName(_fromUtf8("lblHello"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 50, 178, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnHello = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnHello.setObjectName(_fromUtf8("btnHello"))
        self.horizontalLayout.addWidget(self.btnHello)
        self.btnExit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.btnExit.setObjectName(_fromUtf8("btnExit"))
        self.horizontalLayout.addWidget(self.btnExit)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btnExit, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lblHello.setText(_translate("Dialog", "Hello", None))
        self.btnHello.setText(_translate("Dialog", "Hello", None))
        self.btnExit.setText(_translate("Dialog", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

