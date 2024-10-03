import sqlite3

# Connect to the SQLite database (this will create the file 'my_recipes.db')
connection = sqlite3.connect('my_recipes.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL to fill the values in the Users tables
cursor.execute('''
    INSERT INTO Users (UserID, FirstName, LastName, Email, JoinDate)
    VALUES
        (100000, Mike, McCloskey, Mikegmail.com, 2024-09-24);
        (100001, Susan, McCloskey, Mikegmail.com, 2024-09-24);
        (100002, Brittany, Dean, Mikegmail.com, 2024-09-24);
        (100003, Natasha, Roundtree, Mikegmail.com, 2024-09-24);
        (100004, Lindsey, Ort, Mikegmail.com, 2024-09-24);
        (100005, Michaela, O'Connell, Mikegmail.com, 2024-09-24);
        (100006, Matthew, McCloskey, Mikegmail.com, 2024-09-24);
        (100007, Tara, Ferkel, Mikegmail.com, 2024-09-24);
        (100008, Nathan, McCloskey, Mikegmail.com, 2024-09-24);
        (100009, Keira, McCloskey, Mikegmail.com, 2024-09-24);               
''')

# Commit the transaction
connection.commit()

# Close the connection
connection.close()

print("Data imported successfully!")
