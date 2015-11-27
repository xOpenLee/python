#!/usr/bin/env python
# coding=utf-8
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

    
class FontProperiesDlg(QDialog):
    def __init__(self, parent = None):
        super(FontProperiesDlg, self).__init__(parent)
        FontStyleLabel = QLabel(u"中文字体:")
        FontStyleComboBox = QComboBox()
        FontStyleComboBox.addItems([u"宋体", u"黑体", u"仿宋",u"棣书",u"楷体"])
        FontEffectCheckBox = QCheckBox(u"使用特效")
        FontSizeLabel = QLabel(u"字体大小")

        FontSizeSpinBox = QSpinBox()
        FontSizeSpinBox.setRange(1, 90)

        okButton = QPushButton(u"确定")
        cancleButton = QPushButton(u"取消")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancleButton)

        layout = QGridLayout()


        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(FontStyleComboBox, 0, 1)
        
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(FontSizeSpinBox, 1, 1)
        layout.addWidget(FontEffectCheckBox, 1, 2)

        layout.addLayout(buttonLayout, 2, 0)

        self.setLayout(layout)

        self.connect(okButton, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(cancleButton, SIGNAL("clicked()"), self, SLOT("reject()"))

        self.setWindowTitle(u"宋体")

class MainDialog(QDialog):
    def __init__ (self, parent = None):
        super(MainDialog, self).__init__(parent)
        self.FontProperiesDlg = None
        self.format = dict(fontstyle=u"宋体", fontsize = 1, fonteffect = False)
        FontButton1 = QPushButton(u"设置字体(模态)")
        FontButton2 = QPushButton(u"设置字体(非模态)")
        self.label = QLabel(u"默认选择")
        layout = QGridLayout()
        layout.addWidget(FontButton1, 0, 0)
        layout.addWidget(FontButton2, 0, 1)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.connect(FontButton1, SIGNAL("clicked()"), self.FontModalDialog)
        self.connect(FontButton2, SIGNAL("clicked()"), self.FontModalessDialog)
        self.setWindowTitle(u"模态和非模态对话框")
        self.updataData()

    def updataData(self):
        self.label.setText(u"选择的字体: %s<br>字体大小:%d<br>是否特效:%s"
        %(self.format["fontstyle"], self.format["fontsize"], self.format["fonteffect"]))

    def FontModalDialog(self):
        dialog = FontProperiesDlg()

        if dialog.exec_():
            self.format["fontstyle"] = dialog.FontStyleComboBox.currentText()
            self.format["fontsize"] = dialog.FontSizeSpinBox.value()
            self.format["fonteffect"] = dialog.FontEffectCheckBox.isCheck()
            self.updataData()

    def FontModalessDialog(self):
        pass


app = QApplication(sys.argv)
font = MainDialog()
font.show()
app.exec_()


