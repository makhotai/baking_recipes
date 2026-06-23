
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
    user_id INTEGER REFERENCES users,
    created_at TEXT,
    updated_at TEXT
);

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description_r TEXT,
    servings TEXT,
    ingredients TEXT,
    method TEXT,
    user_id INTEGER REFERENCES users,
    created_at TEXT,
    updated_at TEXT
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

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes,
    image BLOB
);

CREATE INDEX idx_recipes_user_id ON recipes (user_id);
CREATE INDEX idx_recipe_classes_recipe_id ON recipe_classes (recipe_id);
CREATE INDEX idx_recipe_classes_title ON recipe_classes (title);
CREATE INDEX idx_reviews_recipe_id ON reviews (recipe_id);
CREATE INDEX idx_images_recipe_id ON images (recipe_id);
