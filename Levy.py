from PySide2.QtWidgets import QApplication, QMainWindow


from levyrekisteri import Ui_LevyRekisteri
#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui

#Luokka sisältää kaikki Levyn tiedot

class Levy():
    def __init__(self):
        super().__init__()
        

        self.ArtistinNimi = ""
        self.LevynNimi = ""
        self.JulkaisuVuosi = ""
        self.Levy_yhtio_painos =""