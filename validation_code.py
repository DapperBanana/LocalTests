
import sqlite3

# Create a new SQLite database connection
conn = sqlite3.connect('test.db')
c = conn.cursor()

# Create a new table
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER NOT NULL)''')

# Create
def create_user(name, age):
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

# Read
def read_users():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)

# Update
def update_user(id, name, age):
    c.execute("UPDATE users SET name=?, age=? WHERE id=?", (name, age, id))
    conn.commit()

# Delete
def delete_user(id):
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()

# Create some initial users
create_user('Alice', 30)
create_user('Bob', 25)

# Display all users
read_users()

# Update user
update_user(1, 'Alice Smith', 32)

# Display all users after update
read_users()

# Delete user
delete_user(2)

# Display all users after delete
read_users()

# Close the database connection
conn.close()
