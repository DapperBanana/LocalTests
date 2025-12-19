// It appears you want C# code, but since the instruction indicates a Python program,
// here is a Python example for performing basic CRUD operations on a SQLite database.

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Insert data (Create)
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))
conn.commit()

# Read data (Read)
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data (Update)
cursor.execute('UPDATE users SET age = ? WHERE name = ?', (31, 'Alice'))
conn.commit()

# Delete data (Delete)
cursor.execute('DELETE FROM users WHERE name = ?', ('Bob',))
conn.commit()

# Verify deletion and update
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
conn.close()