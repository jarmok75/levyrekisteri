from PySide2.QtWidgets import QApplication, QDialog

from levyrekisteri import Ui_LevyRekisteri

from PySide2 import QtCore, QtGui, QtWidgets

from tallenna import Ui_Tallenna

from Levy import Levy



#Luokkaa hoitaa uuden Levyn tallentamisen tiedostoon ja näyttää Kyseisen formin .


class Tallenna_gui(QDialog,Ui_Tallenna):
    def __init__(self):
        super().__init__()
        self.levy = Levy("","","","","")
        

    #Lisää objektit ruudulle määritelty levyrekisteri luokassa
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.tallennaLevy)
        self.buttonBox.rejected.connect(self.close)

    def nayta_formi(self):

        self.tallenna_ikkuna = QDialog()
        self.tallenna_ikkuna = Tallenna_gui()
        self.tallenna_ikkuna.show()

    def tallennaLevy(self):
        #Tallennuksen tarkistukset tänne:

        tarkistus = 0
        
        bandi = self.ArtistinNimi.text()[:20]
        if len(bandi) < 14:
            bandi = bandi + "\t"
        self.levy.ArtistinNimi = bandi

        ln = self.LevynNimi.text()[:20]
        if len(ln) < 14:
            ln = ln + "\t"

        self.levy.LevynNimi = ln
        
        if self.Julkaisuvuosi.text().isnumeric() and len(self.Julkaisuvuosi.text()) < 5:
            self.levy.JulkaisuVuosi = self.Julkaisuvuosi.text()
            tarkistus = 1

        else:
            print("Anna numeerinen lukuarvo tai Luku liian pitkä yli 5 !")
            self.close()
            #Tähän Prompti ikkuna näytölle

        self.levy.Levy_yhtio = self.LevYhtio.text()[:10]
        self.levy.Painos = self.Painos.text()[:14]
        if tarkistus == 1:
            self.tallenna()

    def tallenna(self):

        print ("Tallennetaan levyä..... ", str(self.ArtistinNimi.text()))

        
        rivit = [self.levy.ArtistinNimi, self.levy.LevynNimi, self.levy.JulkaisuVuosi,self.levy.Levy_yhtio, self.levy.Painos ]
        #";".join(str(alkio) for alkio in rivit)
        
 
        #print(rivit)
 

        rivit[4] = str(rivit[4]) + ";"
        #print(rivit)


        with open("levyt.csv", "a") as tiedosto:
            for i in rivit:
                #rivi = ";".join(i)
                rivi = i
                tiedosto.write(rivi+";\t")
            tiedosto.write("\n")


       