from PySide2.QtWidgets import QApplication, QDialog, QMessageBox

from levyrekisteri import Ui_LevyRekisteri

from PySide2 import QtCore, QtGui, QtWidgets

from tallenna import Ui_Tallenna

from Levy import Levy








#Luokkaa hoitaa uuden Levyn tallentamisen tiedostoon ja näyttää Kyseisen formin .


class Tallenna_gui(QDialog,Ui_Tallenna):
    def __init__(self, levy=None):
        super().__init__()
        # self.levy = Levy("","","","","")
        self.levy = levy            #### KRISU: UUSI
        

    #Lisää objektit ruudulle määritelty levyrekisteri luokassa
        self.setupUi(self)
        ##### KRISU: UUSI
        if self.levy:
            self.ArtistinNimi.setText(self.levy.ArtistinNimi)
            self.LevynNimi.setText(self.levy.LevynNimi)
            self.Julkaisuvuosi.setText(self.levy.JulkaisuVuosi)
            self.LevYhtio.setText(self.levy.Levy_yhtio)
            self.Painos.setText(self.levy.Painos)
        ################
        self.buttonBox.accepted.connect(self.tallennaLevy)
        self.buttonBox.rejected.connect(self.reject)            #### KRISU: MUOKATTU

    def nayta_formi(self): # Ei tarvitse

         self.tallenna_ikkuna = QDialog()
         self.tallenna_ikkuna = Tallenna_gui()
         self.tallenna_ikkuna.show()

    def tallennaLevy(self):
        #Tallennuksen tarkistukset tänne:

        ##### KRISU: UUSI
        self.levy.ArtistinNimi = self.ArtistinNimi.text()
        self.levy.LevynNimi = self.LevynNimi.text()
        self.levy.JulkaisuVuosi = self.Julkaisuvuosi.text()
        self.levy.Levy_yhtio = self.LevYhtio.text()
        self.levy.Painos = self.Painos.text()
        #################        
        if True: # KRISU: Jos kaikki hyvin...
            self.accept()
        else:
            pass
            # SHOW ERROR

        # KRISU: En ymmärrä tätä
        # tarkistus = 0
        
        # bandi = self.ArtistinNimi.text()[:20]
        # if len(bandi) < 14:
        #     bandi = bandi + "\t"
        # self.levy.ArtistinNimi = bandi

        # ln = self.LevynNimi.text()[:20]
        # if len(ln) < 14:
        #     ln = ln + "\t"

        # self.levy.LevynNimi = ln
        
        # if self.Julkaisuvuosi.text().isnumeric() and len(self.Julkaisuvuosi.text()) < 5:
        #     self.levy.JulkaisuVuosi = self.Julkaisuvuosi.text()
        #     tarkistus = 1

        # else:
           
        #     #self.close()
        #     #Näytetään virheilmoitus jos vuosiluku ei numeerinen tai yli 5 numeroa pitkä:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Critical)
        #     msg.setText("*** Virhe Vuosiluvussa ***")
        #     msg.setInformativeText('Anna numeerinen lukuarvo tai Luku liian pitkä yli 5 !')
        #     msg.setWindowTitle("*** Error *****")
        #     msg.exec_()

        # self.levy.Levy_yhtio = self.LevYhtio.text()[:10]
        # self.levy.Painos = self.Painos.text()[:14]
        # if tarkistus == 1:
        #     self.tallenna()

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


       