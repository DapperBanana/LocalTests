
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Create function to insert a new user
def insert_user(name, email):
    cursor.execute('''
    INSERT INTO users (name, email) VALUES (?, ?)
    ''', (name, email))
    conn.commit()

# Create function to retrieve all users
def get_users():
    cursor.execute('''
    SELECT * FROM users
    ''')
    users = cursor.fetchall()
    return users

# Create function to update user by id
def update_user(id, name, email):
    cursor.execute('''
    UPDATE users SET name = ?, email = ? WHERE id = ?
    ''', (name, email, id))
    conn.commit()

# Create function to delete user by id
def delete_user(id):
    cursor.execute('''
    DELETE FROM users WHERE id = ?
    ''', (id,))
    conn.commit()

# Example usage
insert_user('Alice', 'alice@example.com')
insert_user('Bob', 'bob@example.com')

print("All users:")
print(get_users())

update_user(1, 'Alice Smith', 'alice.smith@example.com')

print("After update:")
print(get_users())

delete_user(2)

print("After delete:")
print(get_users())

# Close connection
conn.close()
