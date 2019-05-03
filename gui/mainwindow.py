from gui.ui.mainwindow_ui import Ui_MainWindow
from PyQt5 import QtGui, QtWidgets

class ProgramWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
