from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox

from Levy import Levy




#Uuden ikkunan takia
from tallenna import Ui_Tallenna
from tallenna_gui import Tallenna_gui



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
            
        try:
            
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

                    #Lista aakkosjärjestykseen Artistin Nimen perusteella
                    lista.sort(key=lambda s: s.ArtistinNimi)

       
        except IndexError as ie:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("*** Indeksi yli laidan ***")
            msg.setInformativeText("Indeksi yli laidan Poikkeus  ")
            msg.setWindowTitle("*** Poikkeus *****")
            msg.exec_()

                    
        except FileNotFoundError as te:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("*** Tiedotoa ei löydy ***")
            msg.setInformativeText("Wrong file or file path  ")
            msg.setWindowTitle("*** Ei löydy tiedostoa *****")
            msg.exec_()

        return lista
            #Listassa olio lista levyistä

    def MuokkaaLevya(self, muok = []):
            #Ei toimi
            listaa = []
            listaa = self.LueLevyt()
            #Tähän etsintä muokattava 

            if len(muok) == 0:
                return 0
            
            for levy1 in listaa:
                if levy1.ArtistinNimi == muok[0].ArtistinNimi:
                    print("löytyi")
                    Tallenna_gui.nayta_formi(self)
                    #Christian: Miten Formille levy1 tiedot muokkaukseen:?
                    levy1.ArtistinNimi = Tallenna_gui.levy.ArtistinNimi.text()
                    
                    



        #Etsiminen tässä metodissa:
    def Etsi(self, mj = ""):
            #print("Ollaan Hae luokan Etsi levy Funktiossa.... ja etsitään merkkijonoa", mj)
            lista = self.LueLevyt()
             #hakutulosten löytämis lista
            loydetyt = []

            #Jos tyhjä haku palautetaan tyhjä lista, 
            if mj.strip() =="":
                return loydetyt


            #Hakeminen:

            #Käydään olio listaa läpi
            
            for levy in lista:
                #print(levy.ArtistinNimi, " "  ,levy.LevynNimi, " " , levy.JulkaisuVuosi, " " ,  levy.Levy_yhtio, " "  , levy.Painos)
                #Verrataan ArtistinNimeä Haettuun merkkijonoon
                artisti = levy.ArtistinNimi
                levyn_nimi = levy.LevynNimi
                #Löytyykö haettua merkkijonoa mj merkkijonojen artisti tai levyn_nimi sisältä
                if  mj.lower() in artisti.lower() or mj.lower() in levyn_nimi.lower():
                    #print ("Löytyi Haettu artisti tai levy")
                    #Lisätään löydetty levy listaan Artisti nimen tai Levyn nimen  perusteella
                    loydetyt.append(levy)
                loydetyt.sort(key=lambda s: s.ArtistinNimi)
                
            return loydetyt
                

    #Levyn poistaminen listasta
    def PoistaLevy(self, pois=""):
        #print("Ollaan poista levy metodissa")
        poistot = []
        kaikki = []
        #Poistettavat objektit:
        poistot = self.Etsi(pois)
        if len(poistot) > 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("*** Virhe Poistossa ***")
            msg.setInformativeText('Vain yksi Levy Voidaan poistaa kerrallaan')
            msg.setWindowTitle("*** Virhe Poistossa  *****")
            msg.exec_()
    

            return 0
        #Kaikki objektit tässä listassa:
        kaikki = self.LueLevyt()
       
        #Tähän löytyykö poistettava kaikki listasssa, jos löytyy, poistetaan kyseinen objekti listasta:

     
        for levy in kaikki:
            artisti = levy.ArtistinNimi
            levyn_nimi = levy.LevynNimi
            for levy2 in poistot:
                artisti2 = levy2.ArtistinNimi
                levyn_nimi2 = levy2.LevynNimi
                if artisti == artisti2 and levyn_nimi == levyn_nimi2:
                    kaikki.remove(levy)

        #print (kaikki , "testi_poiston jälkeen")

        self.TallennaLista(kaikki)

    def TallennaLista(self, levylista = []):
        #Tänne parametrina tuodun listan tallennus tiedostoon. Käytetään parametria "w" jolloin kirjoitetaan päälle
        with open("levyt.csv", "w") as tiedosto:
            for i in levylista:
                rivit = i.ArtistinNimi +";"+ i.LevynNimi + ";"+ i.JulkaisuVuosi +";" +i.Levy_yhtio +";" +i.Painos 
                
              
                tiedosto.write(rivit+";;\t")
               
                tiedosto.write("\n")  

        