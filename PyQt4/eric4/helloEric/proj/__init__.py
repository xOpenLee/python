import sys
from PyQt4 import QtCore ,  QtGui
import  DlgHelloEric

def main(args):
    app = QtGui.QApplication(sys.argv)
    MainWin = QtGui.QmainWindow()
    Mwin = DlgHelloEric.DlgHelloEric()
    Mwin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv)
