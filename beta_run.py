
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table in the database
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Insert data into the table
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))

# Retrieve data from the table
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

# Update data in the table
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (32, 'Alice'))

# Retrieve updated data from the table
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

# Delete data from the table
cursor.execute('DELETE FROM users WHERE name = ?', ('Bob',))

# Retrieve data after deletion
cursor.execute('SELECT * FROM users')
users = cursor.fetchall()
for user in users:
    print(user)

# Commit the changes and close the connection
conn.commit()
conn.close()
