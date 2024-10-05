#Drop Recipes Table
import sqlite3

# Connect to the SQLite database (this will create the file 'my_recipes.db')
connection = sqlite3.connect('my_recipes.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

try:
    # Drop the old Recipes table
    cursor.execute('DROP TABLE IF EXISTS Recipes')
    
    # Create the new Recipes table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipes (
        RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Description TEXT,
        CookingTime INTEGER,
        Servings INTEGER,
        NumberOfSteps INTEGER,
        SubmittedDate DATE DEFAULT (datetime('now')),
        NumberOfIngredients INTEGER,
        ImageURL TEXT
    )
    ''')

    # Commit the changes
    connection.commit()
    print("Table replaced successfully.")
except Exception as e:
    print(f"An error occurred: {e}")


