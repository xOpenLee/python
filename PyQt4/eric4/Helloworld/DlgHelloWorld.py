# -*- coding: utf-8 -*-

"""
Module implementing DlgHelloWorld.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_DlgHelloWorld import Ui_Dialog

class DlgHelloWorld(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_btnHello_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lblHello.setText("HelloEric")
