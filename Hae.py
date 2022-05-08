from PySide2.QtWidgets import QApplication, QMainWindow
from Levy import Levy




#Uuden ikkunan takia
from tallenna import Ui_Tallenna
#from tallenna_gui import Tallenna_gui



#Luokka hoitaa tiedoston lukemisen ja välittää Nayta luokalle.

class Hae(QMainWindow,Ui_Tallenna):
    def __init__(self):
        super().__init__()
        self.haettavaString = ""
        #self.paaikkuna = MainWindow()

        
    #Tiedoston lukeminen ja palautetaan oliolistana 
    def LueLevyt(self):

        #levylista
        lista = []
            
        with open("levyt.csv") as tiedosto:

            for rivi in tiedosto.readlines():
                uusi_levy = Levy()
                #Tähän miten rivistä saadaan Artisin nimi, Levyn nimi, Julkaisuvuosi, Levy_yht, painos
                uusi_rivi = rivi.split(";")
                    
                uusi_levy.ArtistinNimi = uusi_rivi[0]
                uusi_levy.LevynNimi = uusi_rivi[1]
                uusi_levy.JulkaisuVuosi = uusi_rivi[2]
                uusi_levy.Levy_yhtio = uusi_rivi[3]
                uusi_levy.Painos = uusi_rivi[4]
                lista.append(uusi_levy)
        return lista
            #Listassa olio lista levyistä


        #Etsiminen tässä metodissa:
    def Etsi(self, mj = ""):
            print("Ollaan Hae luokan Etsi levy Funktiossa.... ja etsitään merkkijonoa", mj)
            lista = self.LueLevyt()
             #hakutulosten löytämis lista
            loydetyt = []

            #Jos tyhjä haku palautetaan tyhjä lista, 
            if mj.strip() =="":
                return loydetyt


            #Hakeminen:

            #Käydään olio listaa läpi
            
            for levy in lista:
                print(levy.ArtistinNimi, " "  ,levy.LevynNimi, " " , levy.JulkaisuVuosi, " " ,  levy.Levy_yhtio, " "  , levy.Painos)
                #Verrataan ArtistinNimeä Haettuun merkkijonoon
                artisti = levy.ArtistinNimi
                levyn_nimi = levy.LevynNimi
                #Löytyykö haettua merkkijonoa mj merkkijonojen artisti tai levyn_nimi sisältä
                if  mj.lower() in artisti.lower() or mj.lower() in levyn_nimi.lower():
                    print ("Löytyi Haettu artisti tai levy")
                    #Lisätään löydetty levy listaan Artisti nimen tai Levyn nimen  perusteella
                    loydetyt.append(levy)
                
            return loydetyt
                



    #Saantimetodi tiedoston sisällölle
    def Hae_kaikki(self):
        with open("levyt.csv") as tiedosto:



            sisalto = tiedosto.read()
            #Palauttaa listan
            sisalto2 = sorted(sisalto.split("\n"))
           
            #Lista Sisalto 2 pitäisi saada merkki jono muotoon jotta voidaan näytttää tietoruudulla
            
                
        return sisalto2