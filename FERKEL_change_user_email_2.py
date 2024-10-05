import sqlite3
import pandas as pd

# Step 1: Connect to the SQLite database
connection = sqlite3.connect('my_recipes.db')
cursor = connection.cursor()

# Step 3: Load data into the table
# Example data - Replace with your data source
data = [
    ('900000', 'Mike', 'McCLoskey', 'mike@gmail.com', '9/24/2024'),
    ('900001', 'Susan', 'McCloskey', 'susan@gmail.com', '9/24/2024'),
    ('900002', 'Brittany', 'Dean', 'brittany@gmail.com', '9/24/2024'),
    ('900003', 'Natasha', 'Roundtree', 'natasha@gmail.com', '9/24/2024'),
    ('900004', 'Lindsey', 'Ort', 'lindsey@gmail.com', '9/24/2024'),
    ('900005', 'Michaela', 'OConnell', 'Michaela@gmail.com', '9/24/2024'),
    ('900006', 'Matthew', 'McCloskey', 'Matthew@gmail.com', '9/24/2024'),
    ('900007', 'Tara', 'Ferkel', 'tara@gmail.com', '9/24/2024'),
    ('900008', 'Nathan', 'McCLoskey', 'nathan@gmail.com', '9/24/2024'),
    ('900009', 'Keira', 'McCloskey', 'Keira@gmail.com', '9/24/2024')
]

# Step 4: Insert data into the table
cursor.executemany('''
INSERT INTO Users (UserID, FirstName, LastName, Email, JoinDate) VALUES (?, ?, ?, ?, ?)
''', data)

# Step 5: Commit the transaction and close the connection
connection.commit()
connection.close()

print("Data loaded successfully.")

