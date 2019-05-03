# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tolik/Programs/pyoda/gui/ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_source = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_source.setObjectName("textEdit_source")
        self.horizontalLayout.addWidget(self.textEdit_source)
        self.pushButton_translate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_translate.setObjectName("pushButton_translate")
        self.horizontalLayout.addWidget(self.pushButton_translate)
        self.textEdit_translated = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_translated.setObjectName("textEdit_translated")
        self.horizontalLayout.addWidget(self.textEdit_translated)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Funny Translations"))
        self.pushButton_translate.setText(_translate("MainWindow", "Translate"))


