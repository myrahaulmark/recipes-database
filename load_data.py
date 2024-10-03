import sqlite3
import csv
from pathlib import Path

# Define the path to the data folder
data_folder = Path("P:\\MABA\\Seminar\\recipes database")

# Set the database filename
db_filename = data_folder / "my_recipes.db"

# Set the CSV filename
csv_filename = data_folder / "Categories.csv"

# Connect to the SQLite database
conn = sqlite3.connect(db_filename)

# Create a cursor object
cur = conn.cursor()

# Create the Categories table (if not already created)
cur.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
        CategoryName TEXT NOT NULL
    )
''')

# Open the CSV file and read the data
with open(csv_filename, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # Skip the header row if it exists

    # Insert data into the Categories table
    for row in csv_reader:
        cur.execute('''
            INSERT INTO Categories (CategoryName) 
            VALUES (?)
        ''', (row[0],))  # Assuming the first column is the CategoryName

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Data imported successfully from Categories.csv to the Categories table.")
