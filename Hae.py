from PySide2.QtWidgets import QApplication, QMainWindow
from Levy import Levy


from levyrekisteri import Ui_LevyRekisteri
#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui

#Luokka hoitaa tiedoston lukemisen ja välittää Nayta luokalle.

class Hae(QMainWindow,Ui_Tallenna, Levy):
    def __init__(self):
        super().__init__()