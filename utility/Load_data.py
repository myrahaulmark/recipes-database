import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect("P:\\MABA\\Seminar\\recipes database\\my_recipes.db")

cursor = conn.cursor()

# Step 1: Create a new table with CompID added
cursor.execute('''
CREATE TABLE Category_Recipe_fact_table_new (
    CompID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryID INTEGER,
    RecipeID INTEGER,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID),
    FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID)
);
''')

# Step 2: Copy data from the old table to the new table
cursor.execute('''
INSERT INTO Category_Recipe_fact_table_new (CategoryID, RecipeID)
SELECT CategoryID, RecipeID
FROM Category_Recipe_fact_table;
''')

# Step 3: Drop the old table
cursor.execute('DROP TABLE Category_Recipe_fact_table;')

# Step 4: Rename the new table to the original name
cursor.execute('ALTER TABLE Category_Recipe_fact_table_new RENAME TO Category_Recipe_fact_table;')

# Commit changes and close the connection
conn.commit()
conn.close()
