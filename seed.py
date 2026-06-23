import random
import sqlite3
from werkzeug.security import generate_password_hash

db = sqlite3.connect("database.db")

db.execute("DELETE FROM users")
db.execute("DELETE FROM reviews")
db.execute("DELETE FROM recipes")
db.execute("DELETE FROM recipe_classes")
db.execute("DELETE FROM images")

user_count = 1000
recipe_count = 10**6
review_count = 10**7

for i in range(1, user_count + 1):
    password = "abc" + str(i)
    password_hash = generate_password_hash(password)
    db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
        ["user" + str(i), password_hash])

for i in range(1, recipe_count + 1):
    user_id = random.randint(1, user_count)
    sql = """INSERT INTO recipes (title, description_r,
             servings, ingredients, method, user_id, created_at, updated_at) 
             VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))"""
    result = db.execute(sql, ["title" + str(i), "description_r" + str(i),
                              "servings" + str(i), "ingredients" + str(i), 
                              "method" + str(i), user_id])
    recipe_id = result.lastrowid
    db.execute("INSERT INTO recipe_classes (recipe_id, title) VALUES (?, ?)", [recipe_id, "cakes"])
    db.execute("INSERT INTO recipe_classes (recipe_id, title) VALUES (?, ?)", [recipe_id, "pastries"])
    
for i in range(1, review_count + 1):
    user_id = random.randint(1, user_count)
    recipe_id = random.randint(1, recipe_count)
    rating_review = random.randint(1, 5)

    db.execute("""INSERT INTO reviews
                  (rating_review, text_review, recipe_id, user_id, created_at, updated_at)
                  VALUES (?, ?, ?, ?, datetime('now'), datetime('now'))""",
                  [rating_review, "Very good recipe!",recipe_id, user_id])

db.commit()
db.close()
