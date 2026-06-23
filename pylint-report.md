# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:7:0: E0401: Unable to import 'flask' (import-error)
app.py:8:0: E0401: Unable to import 'flask' (import-error)
app.py:9:0: E0401: Unable to import 'markupsafe' (import-error)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:52:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:80:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:98:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:134:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:156:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:171:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:211:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:211:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:229:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:252:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:268:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:281:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:291:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:295:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:322:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:322:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:345:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:352:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:356:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:2:0: E0401: Unable to import 'flask' (import-error)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:26:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module recipes
recipes.py:1:0: C0114: Missing module docstring (missing-module-docstring)
recipes.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:11:0: R0913: Too many arguments (7/5) (too-many-arguments)
recipes.py:11:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
recipes.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:51:0: R0913: Too many arguments (7/5) (too-many-arguments)
recipes.py:51:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
recipes.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:86:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:92:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:100:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:108:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:112:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:117:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:121:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:130:0: C0116: Missing function or method docstring (missing-function-docstring)
recipes.py:130:0: E0102: function already defined line 30 (function-redefined)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:3:0: E0401: Unable to import 'werkzeug.security' (import-error)
seed.py:13:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:14:0: C0103: Constant name "recipe_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:15:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:1:0: E0401: Unable to import 'werkzeug.security' (import-error)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.64/10 (previous run: 7.61/10, +0.03)
```


## Docstring-ilmoitukset

Suuri osa raportin ilmoituksista on seuraavan tyyppisiä ilmoituksia:

```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
...
```

Nämä ilmoitukset tarkoittavat, että moduuleissa ja funktioissa ei ole docstring-kommentteja. Sovelluksen kehityksessä on tehty tietoisesti päätös, ettei käytetä docstring-kommentteja.

## Import-ilmoitukset

Raportissa on seuraavat ilmoitukset liittyen `import`-komentoihin:

```
app.py:7:0: E0401: Unable to import 'flask' (import-error)
app.py:8:0: E0401: Unable to import 'flask' (import-error)
app.py:9:0: E0401: Unable to import 'markupsafe' (import-error)
...
```

Pylint antaa jostain syystä nämä ilmoitukset, vaikka Flask-kirjasto ja muut kirjastot ovat asennettu kehitysympäristössä. Nämä ilmoitukset eivät haittaa, koska `import`-komennot toimivat sovelluksessa.

## Puuttuva palautusarvo

Raportissa on seuraavat ilmoitukset liittyen funktion palautusarvoon:

```
app.py:211:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:322:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)

```

Nämä ilmoitukset liittyvät tilanteeseen, jossa funktio käsittelee metodit `GET` ja `POST` mutta ei muita metodeja. Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
@app.route("/remove_recipe/<int:recipe_id>", methods=["GET", "POST"])
def remove_recipe(recipe_id):
    require_login()

    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    if request.method == "GET":
        return render_template("remove_recipe.html", recipe=recipe)

    if request.method == "POST":
        if "remove" in request.form:
            recipes.remove_recipe(recipe_id)
            return redirect("/")
        return redirect("/recipe/" + str(recipe_id))
```

Tässä funktio palauttaa arvon, kun `request.method` on `GET` tai `POST`, mutta periaatteessa voisi tulla tilanne, jossa `request.method` on jotain muuta eikä koodi palauttaisi arvoa. Käytännössä tällainen tilanne ei ole kuitenkaan mahdollinen, koska funktion dekoraattorissa on vaatimus, että metodin tulee olla `GET` tai `POST`. Niinpä tässä tapauksessa ei ole riskiä, että funktio ei jossain tilanteessa palauttaisi arvoa.

## Vakion nimi

Raportissa on seuraavat ilmoitukset liittyen vakion nimeen:

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:14:0: C0103: Constant name "recipe_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:15:0: C0103: Constant name "review_count" doesn't conform to UPPER_CASE naming style (invalid-name)

```

Tässä koodin päätasolla määritelty muuttuja tulkitaan vakioksi, jonka nimen tulisi olla kirjoitettu suurilla kirjaimilla. Kuitenkin sovelluksen kehittäjän näkemyksen mukaan tässä tilanteessa näyttää paremmalta, että muuttujan nimi on pienillä kirjaimilla. Muuttujaa käytetään koodissa näin:

```python
app.secret_key = config.secret_key
user_count = 1000
recipe_count = 10**6
review_count = 10**7
```

## Vaarallinen oletusarvo

Raportissa on seuraavat ilmoitukset liittyen vaaralliseen oletusarvoon:

```
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:26:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def execute(sql, params=[]):
    con = get_connection()
    try:
        result = con.execute(sql, params)
        con.commit()
        g.last_insert_id = result.lastrowid
        return result
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()

```

Tässä parametrin oletusarvo `[]` on tyhjä lista. Tässä ongelmaksi voisi tulla, että sama oletusarvona oleva tyhjä listaolio on jaettu kaikkien funktion kutsujen kesken ja jos jossain kutsussa listan sisältöä muutettaisiin, tämä muutos näkyisi myös muihin kutsuihin. Käytännössä tässä tapauksessa tämä ei kuitenkaan haittaa, koska koodi ei muuta listaoliota.

## Liikaa argumentteja

Raportissa on seuraavat ilmoitukset liittyen argumenttien määrään:

```
recipes.py:11:0: R0913: Too many arguments (7/5) (too-many-arguments)
recipes.py:11:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
recipes.py:51:0: R0913: Too many arguments (7/5) (too-many-arguments)
recipes.py:51:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)

```

Esimerkiksi ensimmäinen ilmoitus koskee seuraavaa funktiota:

```python
def add_recipe(title, description_r, servings,
               ingredients, method, user_id, classes):
    sql = """INSERT INTO recipes (title, description_r,
             servings, ingredients, method, user_id, created_at, updated_at) 
             VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))"""
    db.execute(sql, [title, description_r,
                     servings, ingredients, method, user_id])

    recipe_id = db.last_insert_id()
    sql = "INSERT INTO recipe_classes (recipe_id, title) VALUES (?, ?)"
    for class_title in classes:
        db.execute(sql, [recipe_id, class_title])
    return recipe_id

```

Pylint huomautti, että `recipes.add_recipe()`-funktiossa on liikaa argumentteja. Ongelma voitaisiin ratkaista esim. kokoamalla reseptin tiedot yhteen sanakirjaan ja välittämällä ne funktion sisään yhtenä parametrina. Nykyisessä toteutuksessa erilliset argumentit tekevät kuitenkin kutsusta mielestäni selkeämmän ja havainnollisemman, joten ratkaisu jätettiin toistaiseksi tällaiseksi.
