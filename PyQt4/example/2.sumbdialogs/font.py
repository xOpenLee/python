#!/usr/bin/env python
# coding=utf-8
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class FontPropertiesDlg(QDialog):

    def __init__(self, parent=None):
        super(FontPropertiesDlg, self).__init__(parent)
        FontStyleLable = QLabel(u"中文宋体:")
        FontStyleComboBox = QComboBox()
        FontStyleComboBox.addItems([u"宋体", u"黑体", u"仿宋", u"棣书", u"楷体"])

        FontSizeLable = QLabel(u"字体大小")
        FontSizeSpinBox = QSpinBox()
        FontSizeSpinBox.setRange(0, 90)
        FontEffectCheckBox = QCheckBox(u"使用特效")
        okButton = QPushButton(u"确定")
        cancleButton = QPushButton(u"取消")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancleButton)

        layout = QGridLayout()
        layout.addWidget(FontStyleLable, 0, 0)
        layout.addWidget(FontStyleComboBox, 0, 1)
        layout.addWidget(FontSizeLable, 1, 0)
        layout.addWidget(FontSizeSpinBox, 1, 1)
        layout.addWidget(FontEffectCheckBox, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)
        self.setWindowTitle(u"字体")

app = QApplication(sys.argv)
font = FontPropertiesDlg()
font.show()
app.exec_()
