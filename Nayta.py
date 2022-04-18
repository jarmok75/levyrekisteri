from PySide2.QtWidgets import QApplication, QMainWindow

from levyrekisteri import Ui_LevyRekisteri
#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui

#Luokka hoitaa kaikkien tieojen printauksen tietoikkunaan

class Nayta(QMainWindow,Ui_Tallenna):
    def __init__(self):
        super().__init__()


    def Nayta_Tulokset():
        pass