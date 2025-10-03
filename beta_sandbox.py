
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Function to create a new user
def create_user(name, email):
    c.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    print('User created successfully')

# Function to read all users
def read_users():
    c.execute('SELECT * FROM users')
    rows = c.fetchall()
    for row in rows:
        print(row)

# Function to update a user's email
def update_user_email(id, new_email):
    c.execute('UPDATE users SET email = ? WHERE id = ?', (new_email, id))
    conn.commit()
    print('User email updated successfully')

# Function to delete a user
def delete_user(id):
    c.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    print('User deleted successfully')

# Test the CRUD operations
create_user('Alice', 'alice@example.com')
create_user('Bob', 'bob@example.com')

print('All users:')
read_users()

update_user_email(1, 'newalice@example.com')

print('All users after update:')
read_users()

delete_user(2)

print('All users after delete:')
read_users()

# Close the database connection
conn.close()
