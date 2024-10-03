#practice committing a change to the repository

import sqlite3

# Connect to the SQLite database (this will create the file 'my_recipes.db')
connection = sqlite3.connect('my_recipes.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL to create the Categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT NOT NULL
    )
''')

# SQL to create the Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Email TEXT NOT NULL UNIQUE,
        JoinDate DATE DEFAULT (datetime('now'))
    )
''')

# SQL to create the Recipe_Categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipe_Categories (
        CategoryID INTEGER,
        RecipeID INTEGER,
        PRIMARY KEY (CategoryID, RecipeID),
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
        FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID)
    )
''')

# SQL to create the Reviews table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reviews (
        ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
        Rating INTEGER CHECK (Rating >= 1 AND Rating <= 5),
        ReviewText TEXT,
        ReviewDate DATE DEFAULT (datetime('now')),
        UserID INTEGER,
        RecipeID INTEGER,
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID)
    )
''')

# SQL to create the Recipes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipes (
        RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Description TEXT,
        CookingTime INTEGER,
        Servings INTEGER,
        NumberOfSteps INTEGER,
        Instructions TEXT NOT NULL,
        SubmittedDate DATE DEFAULT (datetime('now')),
        NumberOfIngredients INTEGER,
        ImageURL TEXT,
        CategoryID INTEGER,
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    )
''')

# SQL to create the Recipe_Ingredients_fact_table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipe_Ingredients_fact_table (
        CompID INTEGER PRIMARY KEY AUTOINCREMENT,
        RecipeID INTEGER,
        IngredientsID INTEGER,
        Ingredients TEXT,
        FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID),
        FOREIGN KEY (IngredientsID) REFERENCES Ingredients(IngredientsID)
    )
''')

# SQL to create the Ingredients table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ingredients (
        IngredientsID INTEGER PRIMARY KEY AUTOINCREMENT,
        Ingredients TEXT NOT NULL,
        ServingSize REAL,
        Calories REAL,
        TotalFat REAL,
        SaturatedFat REAL,
        Cholesterol REAL,
        Sodium REAL,
        Carbohydrate REAL,
        Fiber REAL,
        Sugars REAL,
        Protein REAL,
        Fat REAL,
        Caffeine REAL,
        Source TEXT,
        Date DATE DEFAULT (datetime('now'))
    )
''')

# Commit the transaction
connection.commit()

# Close the connection
connection.close()

print("Tables created successfully!")
