#!/usr/bin/env python
# coding=utf-8

import sys

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon


def main():
    app = QtGui.QApplication(sys.argv)
    vp = Phonon.VideoPlayer()
    media = Phonon.MediaSource("Eason.mp4")
    vp.show()
    vp.load(media)
    vp.play()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
