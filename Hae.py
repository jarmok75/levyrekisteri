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
        

    def EtsiLevy(self, mj=""):
        #Tänne Levyn / artistin etsintä Tiedostosta
        #Tiedoston luku tänne
        print("Ollaan Hae luokan Etsi levy Funktiossa.... ja etsitään merkkijonoa", mj)

    def Lue_Tiedosto(self):
        lista = []
        
        with open("levyt.csv") as tiedosto:

            for rivi in tiedosto.readlines():
                #Tähän miten rivistä saadaan Artisin nimi, Levyn nimi, Julkaisuvuosi, Levy_yht, painos
                uusi_levy = Levy()
                lista.append(uusi_levy)
            print(lista)
        


    #Saantimetodi tiedoston sisällölle
    def Hae_kaikki(self):
        with open("levyt.csv") as tiedosto:
            sisalto = tiedosto.read()
            sisalto = sisalto.replace(";","\t")
                
        return sisalto