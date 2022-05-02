from posixpath import split
from PySide2.QtWidgets import QApplication, QMainWindow

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


        #Kutsutaan Haku_vali funktiota kun Etsi nappia painetaan
        self.Etsi.clicked.connect(self.Haku_vali)

        
        #Tehkentää haku ja tietoruudun ?
        self.Nollaa.clicked.connect(self.NollaaHaku)

        #Lisää nappi

        self.Lisaa.clicked.connect(self.LisaaLevy)

        #Näytä kaikki nappi:
        self.Naytä_Kaikki_levyt.clicked.connect(self.Hae_Levyt)

        
        #Lisää metodeita

        self.tallenna = Tallenna_gui()

    def Haku_vali(self):

        #Haettu teksti hakukentästä
        haettava = str(self.Hakuruutu.text())

        if haettava =="":
            self.TietoIkkuna.setText("Tähän tulee hakutulokset tai näytetään kaikki levyt valinnan mukaan")

        if haettava !="":
            apu = "Etsitään merkkijonoa " + haettava + "..."
            self.TietoIkkuna.setText(apu)

        

        
        
        
        
        #print(haettava)
        #Kutsutaan Hae luokan Etsilevy funktiota missä etsi tiedostosta etsi toiminnallisuus toteutetaan
        haun_tulos = []
        haun_tulos = self.Haku.EtsiLevy(haettava)
        #Testi print
        print (haun_tulos)
        #Haetun tiedon saaminen TietoIkkunaan:
        tieto =""

        for levy in haun_tulos:
            tieto += levy.ArtistinNimi +"\t"+  levy.LevynNimi + "\t"  +  levy.JulkaisuVuosi + "\t"  + levy.Levy_yhtio +  "\t"  +levy.Painos + "\n"
            
            #self.TietoIkkuna.setText("\n".join(tieto))
        
            


            
        if len(tieto) > 2:
            self.TietoIkkuna.setText(tieto)
        else:
            self.TietoIkkuna.setText("Ei löydy haettua tietoa....")
        


        #Tätä Kutsutaan nyt kun painetaan "Näytä Kaikki levyt" nappia
    def Hae_Levyt(self):
        tieto =""
        self.TietoIkkuna.setText("Haetaan levyjä....")
        sis = self.Haku.Hae_kaikki()


        for rivi in sis:
            #testi = rivi.split(";")
            #pituus = len(testi[0])
            
            #if pituus > 12:
            #        tieto += rivi +"\n"
            #        print (testi[0])
                    
            #else:
            

                tieto += rivi +"\n"
                tieto = tieto.replace(";","\t")

        self.TietoIkkuna.setText(tieto)
        
       
      
        
      


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