import db

def add_recipe(title, description_r,
    servings, ingredients, method, user_id):
    sql = """INSERT INTO recipes (title, description_r,
    servings, ingredients, method, user_id) VALUES (?, ?, ?, ?, ?, ?)"""
    
    db.execute(sql, [title, description_r,
    servings, ingredients, method, user_id])

def get_recipes():
    sql = """SELECT id, title FROM recipes ORDER BY id DESC"""
    return db.query(sql)

def get_recipe(recipe_id):
    sql = """SELECT recipes.id, recipes.title,
    users.username, recipes.description_r,
    recipes.servings, recipes.ingredients, recipes.method,
    users.id user_id
    FROM recipes, users WHERE recipes.user_id = users.id AND recipes.id = ? """
    return db.query(sql, [recipe_id])[0]

def update_recipe(recipe_id, title, description_r, 
    servings, ingredients, method):
    sql = """ UPDATE recipes SET title = ?,
    description_r = ?,
    servings = ?,
    ingredients = ?,
    method = ?
    WHERE id = ?"""
    db.execute(sql, [title, description_r,
    servings, ingredients, method, recipe_id])

def remove_recipe(recipe_id):
    sql = " DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])
