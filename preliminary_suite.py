
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')

# Helper function to insert a user
def insert_user(name, email):
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("User inserted successfully")

# Helper function to retrieve all users
def get_users():
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    if len(users) > 0:
        for row in users:
            print(row)
    else:
        print("No users found")

# Helper function to update a user by ID
def update_user(id, email):
    c.execute("UPDATE users SET email = ? WHERE id = ?", (email, id))
    conn.commit()
    print("User updated successfully")

# Helper function to delete a user by ID
def delete_user(id):
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    print("User deleted successfully")

# Perform CRUD operations
insert_user("John Doe", "john@example.com")
get_users()
update_user(1, "john.doe@example.com")
get_users()
delete_user(1)
get_users()

# Close the connection
conn.close()
