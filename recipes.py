import db

def get_class():
    sql = "SELECT title FROM classes ORDER BY id"
    result = db.query(sql)
    classes = []
    for res in result:
        classes.append(res["title"])
    return classes

def add_recipe(title, description_r,
    servings, ingredients, method, user_id, classes):
    sql = """INSERT INTO recipes (title, description_r,
    servings, ingredients, method, user_id) VALUES (?, ?, ?, ?, ?, ?)"""

    db.execute(sql, [title, description_r,
    servings, ingredients, method, user_id])

    recipe_id = db.last_insert_id()

    sql = """INSERT INTO recipe_classes (recipe_id, title) VALUES (?, ?)"""
    for title in classes:
        db.execute(sql, [recipe_id, title])

def get_classes(recipe_id):
    sql = "SELECT title FROM recipe_classes WHERE recipe_id = ?"
    result = db.query(sql, [recipe_id])
    return [res["title"] for res in result]

def get_recipes():
    sql = """SELECT id, title FROM recipes ORDER BY id DESC"""
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.id, recipes.title,
    users.username, recipes.description_r,
    recipes.servings, recipes.ingredients, recipes.method,
    users.id user_id
    FROM recipes, users WHERE recipes.user_id = users.id AND recipes.id = ? """
    result = db.query(sql, [recipe_id])
    return result[0] if result else None

def update_recipe(recipe_id, title, description_r, 
    servings, ingredients, method, classes):
    sql = """UPDATE recipes SET title = ?,
    description_r = ?,
    servings = ?,
    ingredients = ?,
    method = ?
    WHERE id = ?"""
    db.execute(sql, [title, description_r,
    servings, ingredients, method, recipe_id])

    db.execute("DELETE FROM recipe_classes WHERE recipe_id = ?", [recipe_id])
    sql = "INSERT INTO recipe_classes (recipe_id, title) VALUES (?, ?)"
    for title in classes:
        db.execute(sql, [recipe_id, title])

def remove_recipe(recipe_id):
    sql = " DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])

def find_recipes(query):
    sql = """SELECT id, title
    FROM recipes WHERE title LIKE ? OR description_r LIKE ?
    ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])
