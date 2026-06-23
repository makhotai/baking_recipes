# baking recipes app

* Käyttäjä voi luoda tunnuksen ja kirjautua sovellukseen.
* Käyttäjä voi lisätä sovellukseen leivontareseptejä. Reseptissä näytetään tarvittavat ainekset, annosmäärä, valmistusohjeet, kuvat, luomisaika (ja myös viimeisin muokkausaika, jos reseptiä on muokattu).
* Käyttäjä voi myös muokata ja poistaa lisäämiään reseptejä.
* Käyttäjä näkee sovellukseen lisätyt leivontareseptit, sekä omansa että muiden käyttäjien lisäämät.
* Käyttäjä voi etsiä reseptejä hakusanalla tai kategorian perusteella.
* Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt, listan käyttäjän lisäämistä resepteistä sekä käyttäjän kommenttien määrän.
* Käyttäjä voi valita reseptille yhden tai useamman kategorian (esim. kakkureseptit, makeat leivonnaiset, suolaiset leivonnaiset ja jne).
* Käyttäjä voi antaa reseptille kommentin ja arvosanan. Reseptin yhteydessä näytetään kommentit ja keskimääräinen arvosana.

## Testaus suurella tietomäärällä:
Testauksessa on ajettu seed.py tiedosto
* 1000 käyttäjää
* 10^6 reseptiä
* 10^7 satunnaisesti resepteihin jakautunutta kommenttia

database.db tiedoston koko: **1.15 Gt**

### Sivujen lataamisen sekä metodien ajat

**Etusivun lataaminen**
* "GET / HTTP/1.1" 200: 0.201 s

**Tunnuksen luonti**
* GET /register: 0.0064 s
* POST /create: 0.0982 s

**Kirjautuminen sisään**
* GET /login: 0.0054 s
* POST /login: 0.1079 s

**Reseptin lisäys/muokkaus/poisto**
* GET /new_recipe: 0.013 s
* POST /create_recipe: 0.0153 s
* GET /recipe/1000001: 0.0079 s
* GET /edit_recipe/1000001: 0.0112 s
* POST /update_recipe: 0.0098 s
* GET /remove_recipe/1000001: 0.0129 s
* POST /remove_recipe/1000001: 0.006 s

**Kuvan lisäys/poisto**
* GET /images/1000001: 0.0195 s
* POST /add_image: 0.0095 s
* GET /image/1: 0.0014 s
* POST /remove_images: 0.0029 s

**Kommentin lisäys**
* POST /create_review: 0.0055 s
* GET /recipe/1000000: 0.0128 s

**Käytäjän suvi**
* GET /user/1001: 0.8941 s

**Reseptin etsiminen, GET /find_recipe**
* query "title" (1000000 tulosta): 2.6911 s
* query "t" (1000000 tulosta): 1.985 s
* query "500000" (1 tulos): 1.07 s
* query "abc" (0 tulosta): 0.9006 s
* query_class "cakes" (1000000 tulosta): 1.9292 s
* query_class "savory" (0 tulosta): 0.7707 s

> Näyttää että haku luokan perustella kestää vähemmän aikaa kuin hakusanalla.

Sovellus hidastuu eniten käyttäjäsivulla ja haussa. Syynä voi olla se, että haku käyttää `LIKE`-ehtoa sekä useita ehtoja samassa kyselyssä. Myös käyttäjäsivulla lasketaan reseptit ja arvostelut tietokannasta, mikä voi hidastaa toimintaa suurilla aineistoilla. Indeksit auttavat jonkin verran, mutta kaikki haut eivät silti hyödy niistä yhtä hyvin...

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

### Testaamaan suurella tietomäärällä

Luo ja lisää testidataa tietokantaan:

```
$ python seed.py
```
Se jälkeen voit käynnistää sovelluksen näin:

```
$ flask run
```
