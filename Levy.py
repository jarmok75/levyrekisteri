from PySide2.QtWidgets import QApplication, QMainWindow


from levyrekisteri import Ui_LevyRekisteri
#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui

#Luokka sisältää kaikki Levyn tiedot

class Levy():
    def __init__(self,Artisti="",LevynNimi="",JulkV="",Levy_Yht="",Painos=""):
        super().__init__()
        

        self.ArtistinNimi = Artisti
        self.LevynNimi = LevynNimi
        self.JulkaisuVuosi = JulkV
        self.Levy_yhtio = Levy_Yht
        self.Painos = Painos
        