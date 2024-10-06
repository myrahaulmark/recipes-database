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

    # Manually define data types for each column (foreign keys must be separate)
    columns = {col: data_types.get(col, 'TEXT') for col in headers}

    # Drop the table if it exists
    cur.execute(f'''
        DROP TABLE IF EXISTS {table_name};
    ''')

    # Create the table with foreign key constraints properly defined
    column_defs = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {column_defs},
            FOREIGN KEY (RecipeID) REFERENCES Recipes(RecipeID),  -- RecipeID is correct
            FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)  -- Adjust to match the case if needed
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


# Set the database path
data_folder = Path("P:\\MABA\\Seminar\\recipes database")
db_filename = data_folder / "my_recipes.db"

# Define table schema for Recipe_Ingredients_fact_table (adjust this to match your CSV structure)
data_types = {
    "RecipeID": "INTEGER",             # RecipeID is correct
    "CategoryID": "INTEGER"   
    
}

# This is the actual call to load the data into the new table
load_data(data_folder / "Categories_Recipes_fact_table.csv", db_filename, "Category_Recipe_fact_table", data_types)
