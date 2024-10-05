import sqlite3
import pandas as pd

# Connect to the SQLite database (this will create the file 'my_recipes.db')
connection = sqlite3.connect('my_recipes.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()
             
data = pd.read_sql_query("SELECT * FROM Users", connection)

print(data)

connection.close()