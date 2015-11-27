# -*- coding: utf-8 -*-

"""
Module implementing DlgHelloEric.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_DlgHelloEric import Ui_Dialog

class DlgHelloEric(QDialog, Ui_Dialog):
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
    def on_YesPushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lblHello.setText("HelloEric")
        raise NotImplementedError
