
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')

# Create
def create_user(name, email):
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("User created successfully.")

# Read
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if user:
        print(f"User ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("No user found with that ID.")

# Update
def update_user(user_id, name, email):
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    print("User updated successfully.")

# Delete
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("User deleted successfully.")

# Test the CRUD operations
create_user("Alice", "alice@example.com")
get_user(1)
update_user(1, "Alice Smith", "alice.smith@example.com")
get_user(1)
delete_user(1)
get_user(1)

# Close the connection
conn.close()
