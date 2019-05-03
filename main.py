import sys
from gui.mainwindow import ProgramWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pw = ProgramWindow()
    pw.show()
    sys.exit(app.exec_())
