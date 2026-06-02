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
    servings, ingredients, method, user_id, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))"""

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
    recipes.created_at, recipes.updated_at,
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
    method = ?,
    updated_at = datetime('now')
    WHERE id = ?"""
    db.execute(sql, [title, description_r,
    servings, ingredients, method, recipe_id])

    db.execute("DELETE FROM recipe_classes WHERE recipe_id = ?", [recipe_id])
    sql = "INSERT INTO recipe_classes (recipe_id, title) VALUES (?, ?)"
    for title in classes:
        db.execute(sql, [recipe_id, title])

def remove_recipe(recipe_id):
    sql = " DELETE FROM recipe_classes WHERE recipe_id = ?"
    db.execute(sql, [recipe_id])
    sql = " DELETE FROM recipes WHERE id = ?"
    db.execute(sql, [recipe_id])

def find_recipes(query):
    sql = """SELECT id, title
    FROM recipes WHERE title LIKE ? OR description_r LIKE ?
    ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like])

def add_review(rating_review, text_review, user_id, recipe_id):
    sql = """INSERT INTO reviews (rating_review, text_review, user_id, recipe_id) 
    VALUES (?, ?, ?, ?)"""

    db.execute(sql, [rating_review, text_review, user_id, recipe_id])

def get_reviews(recipe_id):
    sql = """SELECT reviews.id, reviews.rating_review, reviews.text_review,
    users.username, users.id user_id FROM reviews, users
    WHERE reviews.recipe_id = ? AND reviews.user_id=users.id
    ORDER BY reviews.id DESC"""
    return db.query(sql, [recipe_id])

def get_reviews_avg(recipe_id):
    sql = """SELECT id, recipe_id, AVG(rating_review) as avg_r FROM reviews WHERE recipe_id = ?"""
    result = db.query(sql, [recipe_id])
    if result and result[0]["avg_r"] is not None:
        return result[0]["avg_r"]
    else:
        return None

def get_images(recipe_id):
    sql = "SELECT id FROM images WHERE recipe_id = ?"
    return db.query(sql, [recipe_id])

def get_image(image_id):
    sql = "SELECT image from images WHERE id = ?"
    result = db.query(sql, [image_id])
    return result[0][0] if result else None

def add_image(recipe_id, image):
    sql = "INSERT INTO images (recipe_id, image) VALUES (?, ?)"

    db.execute(sql, [recipe_id, image])

def remove_image(recipe_id, image_id):
    sql = "DELETE FROM images WHERE id = ? AND recipe_id = ?"
    db.execute(sql, [image_id, recipe_id])