# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file './tallenna.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

#Importoidaan Qt designer5 tuottama Graaffinen tallenna kaavake, jonka pitäisi näkyä kun pääikkunassa painetaan Lisää nappia


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Tallenna():

    """
    def __init__(self):
        super().__init__()
    """
    def setupUi(self, Tallenna):
        Tallenna.setObjectName("Tallenna")
        Tallenna.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Tallenna)
        self.buttonBox.setGeometry(QtCore.QRect(550, 20, 81, 461))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        #Artistin nimi syöte ruutu
        self.ArtistinNimi = QtWidgets.QLineEdit(Tallenna)
        self.ArtistinNimi.setGeometry(QtCore.QRect(50, 60, 301, 28))
        self.ArtistinNimi.setObjectName("ArtistinNimi")

        #Levyn nimi syöte ruutu
        self.LevynNimi = QtWidgets.QLineEdit(Tallenna)
        self.LevynNimi.setGeometry(QtCore.QRect(50, 130, 301, 28))
        self.LevynNimi.setObjectName("LevynNimi")


        #Julkaisuvuosi syöte ruutu
        self.Julkaisuvuosi = QtWidgets.QLineEdit(Tallenna)
        self.Julkaisuvuosi.setGeometry(QtCore.QRect(50, 190, 151, 28))
        self.Julkaisuvuosi.setObjectName("Julkaisuvuosi")


        #Levy-yhtiö syöte ruutu
        self.LevYhtio = QtWidgets.QLineEdit(Tallenna)
        self.LevYhtio.setGeometry(QtCore.QRect(50, 250, 361, 28))
        self.LevYhtio.setObjectName("LevyYhtio")

        #Painos syöte ruutu
        self.Painos = QtWidgets.QLineEdit(Tallenna)
        self.Painos.setGeometry(QtCore.QRect(50, 310, 361, 28))
        self.Painos.setObjectName("Painos")


        #Artisti Otsikko Teksti:
        self.Artisti_label = QtWidgets.QLabel(Tallenna)
        self.Artisti_label.setGeometry(QtCore.QRect(50, 30, 141, 16))
        self.Artisti_label.setObjectName("Artisti_label")
        
        #Levy_Yhtiö Otsikko Teksti:
        self.Levy_label = QtWidgets.QLabel(Tallenna)
        self.Levy_label.setGeometry(QtCore.QRect(50, 110, 121, 16))
        self.Levy_label.setObjectName("Levy_label")

        #Julkaisuvuosi Otsikko teksti:
        self.Julkaisuvuosi_label = QtWidgets.QLabel(Tallenna)
        self.Julkaisuvuosi_label.setGeometry(QtCore.QRect(50, 170, 81, 16))
        self.Julkaisuvuosi_label.setObjectName("Julkaisuvuosi_label")

        #levy-yhtiö Otsikko Teksti:
        self.Levy_yhtio_label = QtWidgets.QLabel(Tallenna)
        self.Levy_yhtio_label.setGeometry(QtCore.QRect(50, 230, 111, 16))
        self.Levy_yhtio_label.setObjectName("Levy_yhtio_painos_label")

        #Painos Otsikko teksti:
        self.Painos_label = QtWidgets.QLabel(Tallenna)
        self.Painos_label.setGeometry(QtCore.QRect(50, 290, 111, 16))
        self.Painos_label.setObjectName("Levy_yhtio_painos_label")

        self.retranslateUi(Tallenna)
        self.buttonBox.accepted.connect(Tallenna.accept)
        self.buttonBox.rejected.connect(Tallenna.reject)
        QtCore.QMetaObject.connectSlotsByName(Tallenna)

    def retranslateUi(self, Tallenna):
        _translate = QtCore.QCoreApplication.translate
        Tallenna.setWindowTitle(_translate("Tallenna", "Dialog"))
        self.Artisti_label.setText(_translate("Tallenna", "Artistin nimi"))
        self.Levy_label.setText(_translate("Tallenna", "Levyn Nimi"))
        self.Julkaisuvuosi_label.setText(_translate("Tallenna", "Julkaisuvuosi"))
        self.Levy_yhtio_label.setText(_translate("Tallenna", "Levy-yhtiö / Painos"))
        self.Painos_label.setText(_translate("Tallenna", "Painos"))
