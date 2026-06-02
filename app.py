import sqlite3
from flask import Flask
from flask import abort, make_response, redirect, render_template, request, session
import db
import config
import recipes
import users
import re

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_recipes = recipes.get_recipes()
    return render_template("index.html", recipes=all_recipes)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    recipes = users.get_recipes(user_id)
    recipe_count = users.count_recipes(user_id)
    return render_template("show_user.html", user=user, recipes=recipes, recipe_count=recipe_count)

@app.route("/find_recipe")
def find_recipe():
    query = request.args.get("query")
    if query:
        results = recipes.find_recipes(query)
    if not query:
        query = ""
        results = []
    return render_template("find_recipe.html", query=query, results=results)

@app.route("/recipe/<int:recipe_id>")
def show_recipe(recipe_id):
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    classes = recipes.get_classes(recipe_id)
    reviews = recipes.get_reviews(recipe_id)
    rating_avg = recipes.get_reviews_avg(recipe_id)
    images = recipes.get_images(recipe_id)
    return render_template("show_recipe.html", recipe=recipe, classes=classes,
                           reviews=reviews, rating_avg=rating_avg, images=images)

@app.route("/new_recipe")
def new_recipe():
    require_login()
    classes = recipes.get_class()
    return render_template("new_recipe.html", classes=classes)

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    require_login()

    title = request.form["title"]
    if not title or len(title) > 130:
        abort(403)
    description_r = request.form["description_r"]
    if not description_r or len(description_r) > 350:
        abort(403)
    servings = request.form["servings"]
    if not servings or len(servings) > 40:
        abort(403)
    ingredients = request.form["ingredients"]
    if not ingredients or len(ingredients) > 1000:
        abort(403)
    method = request.form["method"]
    if not method or len(method) > 3000:
        abort(403)
    user_id = session["user_id"]

    all_classes = recipes.get_class()
    classes = request.form.getlist("classes")
    for my_class in classes:
        if my_class:
            if my_class not in all_classes:
                abort(403)
    
    recipes.add_recipe(title, description_r,
    servings, ingredients, method, user_id, classes)

    return redirect("/")

@app.route("/create_review", methods=["POST"])
def create_review():
    require_login()

    rating_review = request.form["rating_review"]
    if not re.search("^[[1-5]{0,1}$", rating_review):
        abort(403)
    text_review = request.form["text_review"]
    if not text_review or len(text_review) > 1000:
        abort(403)
    user_id = session["user_id"]
    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(403)

    recipes.add_review(rating_review, text_review,
                       user_id, recipe_id)

    return redirect("/recipe/" + str(recipe_id))

@app.route("/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    require_login()
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)

    all_classes = recipes.get_class()
    selected_classes = recipes.get_classes(recipe_id)
    if selected_classes:
        selected_class = selected_classes[0]
    else:
        selected_class = ""
    return render_template("edit_recipe.html", recipe=recipe, all_classes=all_classes, selected_class=selected_class)

@app.route("/update_recipe", methods=["POST"])
def update_recipe():
    require_login()
    recipe_id = int(request.form["recipe_id"])
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)

    recipe_id = request.form["recipe_id"]
    title = request.form["title"]
    if not title or len(title) > 130:
        abort(403)
    description_r = request.form["description_r"]
    if not description_r or len(description_r) > 350:
        abort(403)
    servings = request.form["servings"]
    if not servings or len(servings) > 40:
        abort(403)
    ingredients = request.form["ingredients"]
    if not ingredients or len(ingredients) > 1000:
        abort(403)
    method = request.form["method"]
    if not method or len(method) > 3000:
        abort(403)
    all_classes = recipes.get_class()
    classes = request.form.getlist("classes")
    for my_class in classes:
        if my_class:
            if my_class not in all_classes:
                abort(403)

    recipes.update_recipe(recipe_id, title, description_r,
    servings, ingredients, method, classes)

    return redirect("/recipe/" + str(recipe_id))

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
        else:
            return redirect("/recipe/" + str(recipe_id))

@app.route("/add_image", methods=["POST"])
def add_image():
    require_login()

    recipe_id = request.form["recipe_id"]
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)
    file = request.files["image"]
    if not file.filename.endswith(".png"):
        return "ERROR: the wrong file format"

    image = file.read()
    if len(image) > 1000 * 1024:
        return "ERROR: the file is too big"

    recipes.add_image(recipe_id, image)
    return redirect("/images/" + str(recipe_id))


@app.route("/images/<int:recipe_id>")
def edit_images(recipe_id):
    require_login()
    recipe = recipes.get_recipe(recipe_id)
    if not recipe:
        abort(404)
    if recipe["user_id"] != session["user_id"]:
        abort(403)

    images = recipes.get_images(recipe_id)

    return render_template("images.html", recipe=recipe, images=images)

@app.route("/image/<int:image_id>")
def show_image(image_id):
    image = recipes.get_image(image_id)
    if not image:
        abort(404)

    response = make_response(bytes(image))
    response.headers.set("Content-Type", "image/png")
    return response

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "ERROR: passwords do not match"
    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "ERROR: the username already exists"
    return """ <p>user account has been created :)</p>
    <p><a href="/">go to main page</a></p>
    <p><a href="/login">log in</a></p> """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "ERROR: the username or/and password are incorrect"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")