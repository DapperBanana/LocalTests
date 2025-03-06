
import sqlite3

# Connect to the database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Insert data
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

# Read data
def read_users():
    users = cursor.execute("SELECT * FROM users").fetchall()
    for user in users:
        print(user)

# Update data
def update_user(user_id, name, email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()

# Delete data
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

# Demo
create_user('John Doe', 'john.doe@example.com')
create_user('Jane Smith', 'jane.smith@example.com')

read_users()

update_user(1, 'John Doe Jr.', 'john.doe.jr@example.com')
read_users()

delete_user(2)
read_users()

# Close the connection
conn.close()
