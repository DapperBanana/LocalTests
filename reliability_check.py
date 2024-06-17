
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insert data into the table
c.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
c.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
conn.commit()

# Read data from the table
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Update data in the table
c.execute("UPDATE users SET email = 'alice@example.org' WHERE name = 'Alice'")
conn.commit()

# Read updated data from the table
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Delete data from the table
c.execute("DELETE FROM users WHERE name = 'Bob'")
conn.commit()

# Read remaining data from the table
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
