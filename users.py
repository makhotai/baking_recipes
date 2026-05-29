import db
from werkzeug.security import check_password_hash, generate_password_hash

def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ? "
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_recipes(user_id):
    sql = "SELECT id, title FROM recipes WHERE user_id = ? ORDER BY id DESC "
    return db.query(sql, [user_id])

def count_recipes(user_id):
    sql = "SELECT COUNT(*) AS recipe_count FROM recipes WHERE user_id = ?"
    result = db.query(sql, [user_id])
    if result and result[0]["recipe_count"] is not None:
        return result[0]["recipe_count"]
    else:
        return None

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])
    if not result:
        return None
    user_id = result[0]["id"]
    password_hash = result[0]["password_hash"]

    if check_password_hash(password_hash, password):
        return user_id
    else:
        return None