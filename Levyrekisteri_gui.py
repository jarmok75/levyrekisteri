from PySide2.QtWidgets import QApplication, QMainWindow

#Importoidaan Qt designer5 tuottama Graaffinen käyttöliittymä aihio
from levyrekisteri import Ui_LevyRekisteri
#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui


class MainWindow(QMainWindow,Ui_LevyRekisteri):
    def __init__(self):
        super().__init__()
        
        #Lisää objektit ruudulle määritelty levyrekisteri luokassa
        self.setupUi(self)
        #Connections
        #Sulkee kentän
        self.Sulje.clicked.connect(self.close)

        #Etsi nappi
        self.Etsi.clicked.connect(self.Hae)

        
        #Tehkentää haku ja tietoruudun ?
        self.Nollaa.clicked.connect(self.NollaaHaku)

        #Lisää nappi

        self.Lisaa.clicked.connect(self.LisaaLevy)

        
        #Lisää metodeita

        self.tallenna = Tallenna_gui()

    def Hae(self):
        
        self.Hakuruutu.setText("Kutsutaan jatkosssa Haku metodia......")
        self.TietoIkkuna.setText("Tähän tulee hakutulokset tai näytetään kaikki levyt valinnan mukaan")


    def NollaaHaku(self):
        self.Hakuruutu.clear()
        self.TietoIkkuna.clear()


    def LisaaLevy(self):
        #Tähän Miten saa Tallenna formi esiin?
        self.tallenna.nayta_formi()


app = QApplication()

ikkuna = MainWindow()
    
ikkuna.show()


app.exec_()