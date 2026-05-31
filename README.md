# baking recipes app

* Käyttäjä voi luoda tunnuksen ja kirjautua sovellukseen.
* Käyttäjä voi lisätä sovellukseen leivontareseptejä. Reseptissä näytetään tarvittavat ainekset, annosmäärä, valmistusohjeet ja kuvat. Lisäksi käyttäjä voi lisätä reseptiin valinnaisia kenttiä, kuten vinkkejä ja ainesosien korvaavia vaihtoehtoja (esim. kananmuna -> pellavansiemenet tekemään vegaaniksi).
* Käyttäjä voi myös muokata ja poistaa lisäämiään reseptejä.
* Käyttäjä näkee sovellukseen lisätyt leivontareseptit, sekä omansa että muiden käyttäjien lisäämät.
* Käyttäjä voi etsiä reseptejä hakusanalla tai kategorian perusteella.
* Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt, listan käyttäjän lisäämistä resepteistä sekä käyttäjän kommenttien määrän.
* Käyttäjä voi valita reseptille yhden tai useamman kategorian (esim. kakkureseptit, makeat leivonnaiset, suolaiset leivonnaiset ja jne).
* Käyttäjä voi antaa reseptille kommentin (johon voi liittää kuvan) ja arvosanan tai esittää reseptiin liittyvän kysymyksen. Reseptin yhteydessä näytetään kommentit ja keskimääräinen arvosana.

## Välipalautus 2 (31.05)
Sovelluksen ulkoasu on vielä hyvin pelkistetty, koska en ole vielä ehtinyt tehdä varsinaista tyylittelyä. Tällä hetkellä sivujen HTML-rakenne toimii, mutta visuaalinen viimeistely on vielä kesken.
### Pakkoliset toiminnot:
* **Käyttäjä voi luoda tunnuksen ja kirjautua sovellukseen.**
Jos käyttäjä ei ole kirjautunut sisään, etusivulla näkyvät linkit **log in**, **register** ja **search recipe**, sekä lisättyjen reseptien lista, jos reseptejä on olemassa.  
Jos käyttäjä on kirjautunut sisään, etusivulla näkyvät linkit **log out**, **add new recipe** ja **search recipe**, sekä lisättyjen reseptien lista, jos reseptejä on olemassa.

* **Käyttäjä voi lisätä, muokata ja poistaa leivontareseptejä.** Reseptin kentät ovat nimi, kuvaus, kategoria, tarvittavat ainekset, annosmäärä ja valmistusohjeet. Kaikki kentät ovat pakollisia sekä lisäyksessä että muokkauksessa.  
Sovellus tarkistaa myös syötteiden pituudet, ja jos käyttäjä yrittää kiertää tarkistuksia esimerkiksi DevToolsilla, sovellus palauttaa virheen 403.  
Käyttäjä voi muokata ja poistaa vain omia reseptejään. Jos käyttäjä yrittää avata toisen käyttäjän reseptin muokkaussivun esimerkiksi vaihtamalla url osoitetta, sovellus palauttaa virheen 403.  
Jos reseptiä ei ole olemassa, sovellus palauttaa virheen 404.  
Reseptin sivulla näkyy myös reseptin julkaisuaika (ja jos reseptiä on muokattu, näkyy myös muokkausaika).

* **Käyttäjä näkee sovellukseen lisätyt leivontareseptit, sekä omansa että muiden käyttäjien lisäämät.** Reseptin sivulla näytetään reseptin tekijä, keskiarvoinen arvosana, kuvaus, kategoria, annosmäärä, tarvittavat ainekset ja valmistusohjeet.  
Jos resepti kuuluu kirjautuneelle käyttäjälle, sivulla näkyvät linkit **edit recipe** ja **remove recipe**.  
Jos resepti kuuluu jollekin toiselle käyttäjälle, sivulla näkyy **write a review** lomake. Lomakkeella voi antaa arvosanan välillä 1–5 sekä kirjoittaa kommentin.  
Reseptin sivulla näkyy myös osio **comments and reviews**, jossa näytetään arvostelun tekijä, arvosana ja kommentin teksti.

* **Käyttäjä voi etsiä reseptejä hakusanalla.** Etusivulla on linkki **search recipe**, joka vie hakusivulle `/find_recipe`. Reseptiä voi etsiä ainakin nimen ja kuvauksen perusteella.
### Lisäksi voi testata: 
* **Käyttäjän sivu**. Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt ("user has not published recipes yet"/"user published 1 recipe:"/"user published {count} recipes:") ja listan käyttäjän lisäämistä resepteistä. Jos käyttäjää ei ole olemassa, sovellus palauttaa virheen 404.

## Sovelluksen asennus
Asenna `flask`-kirjasto:

```
$ pip install flask
```
Tietokantatiedosto **database.db** ei kuulu repositorioon, joten testaajan pitää luoda se itse .sql-tiedostojen perusteella.


Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
