Projekti suunnitelma Levyrekisteri


Toteutetaan Levyrekisteri ohjelma Python ohjelmointikielellä. Ohjelma tallentaa levyn tiedot tiedostoon ja lukee musiikki levyjen tiedot tiedostosta annettujen hakuehtojen perusteella. Alustavasti hakuehtoina Artistin nimi tai osa siitä tai levyn nimi tai osa siitä. Ohjelmaan toteutetaan graafinen käyttöliittymä, jossa on hakutoiminto ja mahdollisuus tallettaa uuden levyn tiedot CSV-tiedostoon. Toteutetaan myös levyn tietojen muokkaus ja yksittäisen levyn poistaminen listalta. Jos aikaa jää toteutetaan tietokanta luku/tallennus. Sekä levyjen kansikuvien haku/tallennus.

Vaatimukset:
-Mahdollisuus tallettaa Levyn tiedot tiedostoon.
-Ohjelma lukee Levyn tiedot tiedostosta.
-Ohjelmassa haku toiminto, jossa mahdollista etsitä levyjä/levy tiedostosta:
	- Artistin nimen perusteella tai osan nimestä s.e:
	Frank Zappa ja Zappa tuottavat saman haku tulokset
	-Levyn nimen perusteella tai osan nimestä:
	Tuloksena yhden levyn tiedot.

Viikkosuunnitelma: 
Viikko1:	Luokkien ja muuttujien suunnittelu. Luokkien ja muuttujien toteutus.

Viikko2: 	Tiedon tallentaminen cvs- tiedostoon.

Viikko3: 	Tiedon lukeminen rivettäin readlines() Funkitiolla ja tietojen pilkkominen levy Olioon.
            Haku Metodin toteuttaminen s.e haku kentään syötetyn merkkijonon perusteella etsitään tiedostosta rivi kerrallaan löytyykö. Jos löytyy luodaan uusi lista löytyneistä. Löytynyt lista näytetään tietoruudulla.
	
Viikko4: Levyjen näytön korjaus tasamittaiseksi Graffisen käyttöliittymän tietoruudulla


 
UserStory1

Käyttäjä haluaa Tallettaa uuden levyn tiedot:
Paina lisää nappia
Syötä Formille Levyn tiedot: Artistin nimi, Levyn nimi, Julkaisuvuosi, Levy-yhtiö ja Painos tiedot
Ok Tallentaa tiedot 

User Story2:

Käyttäjä haluaa Katsoa kaikki levyt rekisteristä:
Paina Näytä kaikki levyt nappia

User Strory3:

Käyttäjä haluaa etsiä tietyn levyn tiedot:
Käyttäjä kirjoittaa haettavan Artistin tai levyn nimen LineEdit- Boxiin ja tulokset tulevat näkyviin kun käyttäjä painaa Hae nappia.
Jatkossa Tietoruutu päivittyy kun tekstiä kirjoitetaan ilman Hae napin painamista ( Jos jää aikaa).

User Story4:
(Jatko kehitys Idea)
Levyn tietojen muokkaus:
Käyttäjä hakee levyn tiedot kuten edellä ja valitsee jotenkin levyn tietoruudulta ja painaa Muokkaa nappia.
Levyn tiedot Form esiin ja Ok tallennus.



