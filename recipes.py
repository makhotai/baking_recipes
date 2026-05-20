import db
import sqlite3


def add_recipe(title, description_r, 
    servings, ingredients, method, user_id):
    sql = """INSERT INTO recipes (title, description_r, 
    servings, ingredients, method, user_id) VALUES (?, ?, ?, ?, ?, ?)"""
    
    db.execute(sql, [title, description_r, 
    servings, ingredients, method, user_id])
    