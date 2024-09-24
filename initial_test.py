
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data
c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Retrieve data
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Update data
c.execute("UPDATE users SET age = 28 WHERE name = 'Alice'")

# Retrieve updated data
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Delete data
c.execute("DELETE FROM users WHERE name = 'Bob'")

# Retrieve remaining data
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Commit changes and close connection
conn.commit()
conn.close()
