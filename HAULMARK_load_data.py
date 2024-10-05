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
data_folder = Path("P:\\MABA\\Seminar\\recipes database\\Data_files")
db_filename = data_folder / "my_recipes.db"

# Define table schema for Ingredients table (adjust this to match your CSV structure)
data_types = {
    "IngredientsID": "INTEGER PRIMARY KEY",
    "Ingredients": "TEXT NOT NULL",
    "ServingSize": "INTEGER",
    "Calories": "INTEGER",
    "TotalFat": "INTEGER",
    "SaturatedFat": "INTEGER",
    "Cholesterol": "INTEGER",
    "Sodium": "INTEGER",
    "Carbohydrate": "INTEGER",
    "Fiber": "INTEGER",
    "Sugars": "INTEGER",
    "Protein": "INTEGER",
    "Fat": "INTEGER",
    "Caffeine": "INTEGER",
    "Source": "TEXT",
    "Date": "TEXT",
    "IsAllergen": "TEXT",
    "Food_allergen_ID": "INTEGER",
    "Food": "TEXT",
    "Food_Class": "TEXT",
    "Food_type": "TEXT",
    "Food_Group": "TEXT",
    "Allergy_Type": "TEXT"
}

# This is the actual call to load the data into the Ingredients table
load_data(data_folder / "Ingredients.csv", db_filename, "Ingredients", data_types)
