# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './levyrekisteri.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_LevyRekisteri(object):
    def setupUi(self, LevyRekisteri):
        LevyRekisteri.setObjectName("LevyRekisteri")
        LevyRekisteri.resize(924, 655)
        self.centralwidget = QtWidgets.QWidget(LevyRekisteri)
        self.centralwidget.setObjectName("centralwidget")
        self.TietoIkkuna = QtWidgets.QTextBrowser(self.centralwidget)
        self.TietoIkkuna.setGeometry(QtCore.QRect(60, 170, 601, 381))
        self.TietoIkkuna.setObjectName("TietoIkkuna")
        self.Etsi = QtWidgets.QPushButton(self.centralwidget)
        self.Etsi.setGeometry(QtCore.QRect(340, 50, 90, 28))
        self.Etsi.setObjectName("Etsi")
        self.Hakuruutu = QtWidgets.QLineEdit(self.centralwidget)
        #self.Hakuruutu = QtWidgets.QTextBrowser(self.centralwidget)
        self.Hakuruutu.setGeometry(QtCore.QRect(60, 40, 241, 41))
        self.Hakuruutu.setObjectName("Hakuruutu")
        self.Sulje = QtWidgets.QPushButton(self.centralwidget)
        self.Sulje.setGeometry(QtCore.QRect(810, 550, 90, 28))
        self.Sulje.setObjectName("Sulje")
        self.Nollaa = QtWidgets.QPushButton(self.centralwidget)
        self.Nollaa.setGeometry(QtCore.QRect(570, 50, 81, 31))
        self.Nollaa.setObjectName("Nollaa")
        self.Lisaa = QtWidgets.QPushButton(self.centralwidget)
        self.Lisaa.setGeometry(QtCore.QRect(450, 50, 101, 28))
        self.Lisaa.setObjectName("Lisaa")
        LevyRekisteri.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LevyRekisteri)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        LevyRekisteri.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LevyRekisteri)
        self.statusbar.setObjectName("statusbar")
        LevyRekisteri.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        

        self.retranslateUi(LevyRekisteri)
        QtCore.QMetaObject.connectSlotsByName(LevyRekisteri)

    def retranslateUi(self, LevyRekisteri):
        _translate = QtCore.QCoreApplication.translate
        LevyRekisteri.setWindowTitle(_translate("LevyRekisteri", "MainWindow"))
        self.Etsi.setText(_translate("LevyRekisteri", "Etsi"))
        self.Sulje.setText(_translate("LevyRekisteri", "Sulje"))
        self.Nollaa.setText(_translate("LevyRekisteri", "Nollaa"))
        self.Lisaa.setText(_translate("LevyRekisteri", "Lisää"))
        self.menuFile.setTitle(_translate("LevyRekisteri", "File"))
