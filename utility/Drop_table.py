import sqlite3
from pathlib import Path

# Define the path to the database
data_folder = Path("P:\\MABA\\Seminar\\recipes database")
db_filename = data_folder / "my_recipes.db"

# Connect to the SQLite database
conn = sqlite3.connect(db_filename)

# Create a cursor object
cur = conn.cursor()

# Drop the Ingredients table if it exists
cur.execute('''
    DROP TABLE IF EXISTS Ingredients;
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()

print("Ingredients table has been dropped successfully.")
