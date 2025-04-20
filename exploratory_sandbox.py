
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Function to insert a new record
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# Function to read all records
def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to update a record
def update_user(id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()

# Function to delete a record
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()

# Perform CRUD operations
create_user('Alice', 25)
create_user('Bob', 30)

read_users()

update_user(1, 'Alice Smith', 26)

delete_user(2)

read_users()

conn.close()
