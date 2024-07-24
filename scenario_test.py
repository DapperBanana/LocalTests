
import sqlite3

# Function to create a new table in the database
def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert a new record into the database
def insert_record(name, email):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

# Function to read all records from the database
def read_records():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to update a record in the database
def update_record(id, name, email):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, id))
    conn.commit()
    conn.close()

# Function to delete a record from the database
def delete_record(id):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Main program
create_table()
insert_record('Alice', 'alice@example.com')
insert_record('Bob', 'bob@example.com')

print("All records:")
print(read_records())

update_record(1, 'Alice Smith', 'alice.smith@example.com')

print("After update:")
print(read_records())

delete_record(2)

print("After delete:")
print(read_records())
