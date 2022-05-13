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
        
        bandi = self.ArtistinNimi.text()
        if len(bandi) < 14:
            bandi = bandi + "\t"
        self.levy.ArtistinNimi = bandi

        ln = self.LevynNimi.text()
        if len(ln) < 14:
            ln = ln + "\t"

        self.levy.LevynNimi = ln
        self.levy.JulkaisuVuosi = self.Julkaisuvuosi.text()
        self.levy.Levy_yhtio = self.LevYhtio.text()
        self.levy.Painos = self.Painos.text()
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


       