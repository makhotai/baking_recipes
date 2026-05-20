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
    sql = """SELECT recipes.title, users.username, recipes.description_r,
    recipes.servings, recipes.ingredients, recipes.method
    FROM recipes, users WHERE recipes.user_id = users.id AND recipes.id = ? """
    return db.query(sql, [recipe_id])[0]
    