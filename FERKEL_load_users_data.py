import sqlite3
import csv
from pathlib import Path

# Define the load_data function
def load_data(csv_filename, db_filename, table_name, data_types):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_filename)
    cur = conn.cursor()

    # Open the CSV file and read the header for column names
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)  # Use the header row to define column names

    # Manually define data types for each column (this part is still manual)
    columns = {col: data_types.get(col, 'TEXT') for col in headers}
   
    #DROP the table if it already exists
    cur.execute("DROP TABLE IF EXISTS Users")

    # Create the table if it doesn't exist
    column_defs = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {column_defs}
        )
    ''')

    # Insert data into the table
    placeholders = ', '.join(['?' for _ in columns])
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            cur.execute(f'''
                INSERT INTO {table_name} ({', '.join(columns.keys())}) 
                VALUES ({placeholders})
            ''', row)

    # Commit and close
    conn.commit()
    conn.close()

    print(f"Data imported successfully from {csv_filename} to the {table_name} table.")


# This part goes **outside** the function definition
# Set the database path
#data_folder = Path("P:\\MABA\\Seminar\\recipes database\\Data_files")
data_folder = Path("C:\\Users\\JBAFNLE3\\OneDrive - J.B. Hunt Transport\\Documents\\Personal\\Grad School\\Fall 2024\\Seminar in IS Topics\\Recipe Project\\Clean Data Tables\\2024.09.24 Recipes Dimension - clean.csv")
db_filename = data_folder / "my_recipes.db"

# Define table schema for Ingredients table (adjust this to match your CSV structure)
data_types = {
    "UserID": "INTEGER PRIMARY KEY",
    "FirstName": "TEXT NOT NULL",
    "LastName": "TEXT NOT NULL",
    "Email": "TEXT NOT NULL",
    "JoinDate": "DATE DEFAULT (datetime('now'))"
}

# This is the actual call to load the data into the Users table
load_data(data_folder / "Users.csv", db_filename, "Users", data_types)