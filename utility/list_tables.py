import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('my_recipes.db')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Query to list all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all results and print them
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
connection.close()

