
import sqlite3


def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()


def insert_user(name, age):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users


def update_user(user_id, name, age):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
    conn.commit()
    conn.close()


def delete_user(user_id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()


# Create table
create_table()

# Insert a user
insert_user('Alice', 25)

# Get all users
print(get_users())

# Update a user
update_user(1, 'Alice Smith', 26)

# Get all users
print(get_users())

# Delete a user
delete_user(1)

# Get all users
print(get_users())
