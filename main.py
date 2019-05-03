import sys
from gui.mainwindow import ProgramWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pw = ProgramWindow()
    pw.show()
    sys.exit(app.exec_())
