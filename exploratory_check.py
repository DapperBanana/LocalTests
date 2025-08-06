
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('sample.db')
cursor = connection.cursor()

# Create table
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')

# Insert data
cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('John Doe', 'johndoe@example.com'))

# Select data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data
cursor.execute('UPDATE users SET email = ? WHERE name = ?', ('johndoe@gmail.com', 'John Doe'))

# Delete data
cursor.execute('DELETE FROM users WHERE name = ?', ('John Doe',))

# Commit changes and close connection
connection.commit()
connection.close()
