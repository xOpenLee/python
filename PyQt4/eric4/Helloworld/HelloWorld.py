import sys
from PyQt4 import QtCore, QtGui
import DlgHelloWorld
 
def main(args):
    app = QtGui.QApplication(sys.argv)
    MainWin = QtGui.QMainWindow()
    Mwin = DlgHelloWorld.DlgHelloWorld()
    Mwin.show()
    sys.exit(app.exec_())
 
if __name__=="__main__":
    main(sys.argv)
