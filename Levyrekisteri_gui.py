from posixpath import split
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

#Importoidaan Qt designer5 tuottama Graaffinen käyttöliittymä aihio
from levyrekisteri import Ui_LevyRekisteri
#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui
from Hae import Hae


class MainWindow(QMainWindow,Ui_LevyRekisteri):
    def __init__(self):
        super().__init__()


        #Tuodaan Hae luokan ilmentymä
        self.Haku = Hae()
        
        #Lisää objektit ruudulle määritelty levyrekisteri luokassa
        self.setupUi(self)
        #Connections
        #Sulkee kentän
        self.Sulje.clicked.connect(self.close)


        #Nappuloiden painamisen kuuntelijat:

        #Etsi nappi:
        self.Etsi.clicked.connect(self.Haku_vali)

        
        #Tehkentää haku ja tietoruudun ?
        self.Nollaa.clicked.connect(self.NollaaHaku)

        #Lisää nappi

        self.Lisaa.clicked.connect(self.LisaaLevy)

        #Näytä kaikki nappi:
        self.Naytä_Kaikki_levyt.clicked.connect(self.Hae_Levyt)

        #Poista Nappi:

        self.Poista.clicked.connect(self.Poisti_vali)

        #Muokkaa nappi:

        self.Muokkaa.clicked.connect(self.Muokkaa_vali)

        
        #Lisää metodeita

        self.tallenna = Tallenna_gui()

    def Muokkaa_vali(self):
        #Täällä ollaan kun painetaan Muokkaa- nappia
        
        self.TietoIkkuna.setText("Muokkaus toiminto odottaa toteutusta...")
        haettava = str(self.Hakuruutu.text())

        if len(haettava.strip()) < 2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("*** Virhe Muokkauksessa ***")
            msg.setInformativeText('Etsi ensiksi poistettava levy ')
            msg.setWindowTitle("*** Käytä Hakua *****")
            msg.exec_()
            self.Hakuruutu.clear()
            self.TietoIkkuna.clear()
            return 0      

        muokattavat = []
        muokattavat = self.Haku.Etsi(haettava)
        
        
        if len(muokattavat) > 1:
            print("")
            self.TietoIkkuna.setText("Muokkaus toiminto odottaa toteutusta...")
        else:
            self.Haku.MuokkaaLevya(muokattavat)
        


    def Poisti_vali(self):
        #print("Ollaan poisto napin vali metodissa")
        poistettava = str(self.Hakuruutu.text())

        if len(poistettava.strip()) < 2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("*** Virhe Poistossa ***")
            msg.setInformativeText('Tee Ensin haku')
            msg.setWindowTitle("*** Tyhjä hakukenttä  *****")
            msg.exec_()
            self.Hakuruutu.clear()
            return 0
        self.Haku.PoistaLevy(poistettava)
        
        msg2 = QMessageBox()
        msg2.setIcon(QMessageBox.Information)
        msg2.setText("*** Poisto Onnistui ***")
        msg2.setInformativeText('Levy on poistettu. ')
        msg2.setWindowTitle("*** Poisto OK *****")
        msg2.exec_()
        
        self.Hakuruutu.clear()
        self.TietoIkkuna.clear()

    def Haku_vali(self):

        #Haettu teksti hakukentästä
        haettava = str(self.Hakuruutu.text())

       

        
        
        if len(haettava.strip()) < 2:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("*** Virhe Hakemisessa ***")
            msg.setInformativeText('Täytä esin haku kenttä')
            msg.setWindowTitle("*** Tyhjä hakukenttä  *****")
            msg.exec_()
            self.Hakuruutu.clear()
            return 0
        
        if haettava !="":
            apu = "Etsitään merkkijonoa " + haettava + "..."
            self.TietoIkkuna.setText(apu)
        
        #Kutsutaan Hae luokan Etsilevy funktiota missä etsi tiedostosta etsi toiminnallisuus toteutetaan
        haun_tulos = []
        haun_tulos = self.Haku.Etsi(haettava)
        #Testi print
        #print (haun_tulos)
        #Haetun tiedon saaminen TietoIkkunaan:
        tieto =""

        for levy in haun_tulos:
            tieto += levy.ArtistinNimi +"\t"+  levy.LevynNimi + "\t"  +  levy.JulkaisuVuosi + "\t"  + levy.Levy_yhtio +  "\t"  +levy.Painos + "\n"
            
            #self.TietoIkkuna.setText("\n".join(tieto))
        
            
            
        if len(tieto) > 2:
            self.TietoIkkuna.setText(tieto)
        else:
            self.TietoIkkuna.setText("Ei löydy haettua tietoa....")
            self.Hakuruutu.clear()
        


        #Tätä Kutsutaan nyt kun painetaan "Näytä Kaikki levyt" nappia
    def Hae_Levyt(self):

        """
        tieto =""
        self.TietoIkkuna.setText("Haetaan levyjä....")
        sis = self.Haku.Hae_kaikki()


        for rivi in sis:


                tieto += rivi +"\n"
                tieto = tieto.replace(";","\t")

        self.TietoIkkuna.setText(tieto)

        """
        haun_tulos = []
        haun_tulos = self.Haku.LueLevyt()
        
        tieto =""

        for levy in haun_tulos:
            tieto += levy.ArtistinNimi +"\t"+  levy.LevynNimi + "\t"  +  levy.JulkaisuVuosi + "\t"  + levy.Levy_yhtio +  "\t"  +levy.Painos + "\n"
            
        
        
            
        if len(haun_tulos) > 0:
            self.TietoIkkuna.setText(tieto)
        else:
            self.TietoIkkuna.setText("Ei löydy haettua tietoa....")
            self.Hakuruutu.clear()
       
      
        
      


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