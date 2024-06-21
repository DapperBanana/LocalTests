
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')

# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")
conn.commit()

# Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Users:")
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE users SET email = 'alice@gmail.com' WHERE name = 'Alice'")
conn.commit()

# Retrieve updated data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("\nUsers after update:")
for row in rows:
    print(row)

# Delete data
cursor.execute("DELETE FROM users WHERE name = 'Bob'")
conn.commit()

# Retrieve data after deletion
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("\nUsers after deletion:")
for row in rows:
    print(row)

# Close the connection
conn.close()
