
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    rating_review INTEGER,
    text_review TEXT,
    recipe_id INTEGER REFERENCES recipes,
    user_id INTEGER REFERENCES users
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description_r TEXT,
    servings TEXT,
    ingredients TEXT,
    method TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE recipe_classes (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    title TEXT
);