import requests, json
from gui.ui.mainwindow_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, pyqtSignal

class ProgramWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_translate.clicked.connect(self.onTranslateClick)

    @pyqtSlot()
    def onTranslateClick(self):
        toBeTranslated = self.ui.textEdit_source.toPlainText()
        if len(toBeTranslated) < 1:
            mb = QtWidgets.QMessageBox()
            mb.setText('You should yodify SOMETHING!')
            mb.exec()
        else:
            url = 'https://api.funtranslations.com/translate/yoda.json'
            payload = { 'text': toBeTranslated }
            response = requests.post(url, data=payload)
            if response.ok:
                data = json.loads(response.content)
                self.ui.textEdit_translated.setText(data['contents']['translated'])
            else:
                response.raise_for_status()

