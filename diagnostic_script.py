
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    email TEXT
                )''')

# Insert data
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ('Alice', 25, 'alice@example.com'))
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ('Bob', 30, 'bob@example.com'))

# Perform read operation
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, 'Alice'))

# Perform read operation
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Delete data
cursor.execute("DELETE FROM users WHERE name = ?", ('Bob',))

# Perform read operation
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()
