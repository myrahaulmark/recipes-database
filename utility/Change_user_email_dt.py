import sqlite3

# Connect to the SQLite database (this will create the file 'my_recipes.db')
connection = sqlite3.connect('my_recipes.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL to create the Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Email VARCHAR(100) NOT NULL UNIQUE,
        JoinDate DATE DEFAULT (datetime('now'))
    )
''')

# Commit the transaction
connection.commit()

# Close the connection
connection.close()

print("Tables created successfully!")
