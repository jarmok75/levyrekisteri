from PySide2.QtWidgets import QApplication, QDialog

from levyrekisteri import Ui_LevyRekisteri

from PySide2 import QtCore, QtGui, QtWidgets

from tallenna import Ui_Tallenna

#from Levy import Levy



#Luokkaa hoitaa uuden Levyn lisäämisen tiedostoon ja näyttää Kyseisen formin.


class Tallenna_gui(QDialog,Ui_Tallenna):
    def __init__(self):
        super().__init__()

    #Lisää objektit ruudulle määritelty levyrekisteri luokassa
        self.setupUi(self)


    def nayta_formi(self):

        self.tallenna_ikkuna = QDialog()
        self.tallenna_ikkuna = Tallenna_gui()
        self.tallenna_ikkuna.show()



       