
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Create operation
def create_user(name, age):
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("User created successfully")

# Read operation
def read_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# Update operation
def update_user(id, name, age):
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()
    print("User updated successfully")

# Delete operation
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    print("User deleted successfully")

# Test the CRUD operations
create_user("Alice", 25)
create_user("Bob", 30)
read_users()
update_user(1, "Alice Smith", 30)
delete_user(2)
read_users()

# Close the database connection
conn.close()
