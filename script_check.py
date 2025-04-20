
import sqlite3

# Function to create a new database
def create_database():
    conn = sqlite3.connect('mydatabase.db')
    print("Database created successfully")
    conn.close()

# Function to create a new table
def create_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    print("Table created successfully")
    conn.close()

# Function to insert data into the table
def insert_data(name, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("Data inserted successfully")
    conn.close()

# Function to read data from the table
def read_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Function to update data in the table
def update_data(id, name, email):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, id))
    conn.commit()
    print("Data updated successfully")
    conn.close()

# Function to delete data from the table
def delete_data(id):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    print("Data deleted successfully")
    conn.close()

# Main function to demonstrate CRUD operations
if __name__ == "__main__":
    create_database()
    create_table()

    insert_data("Alice", "alice@example.com")
    insert_data("Bob", "bob@example.com")
    
    read_data()

    update_data(1, "Alice Smith", "alice.smith@example.com")
    
    read_data()

    delete_data(2)
    
    read_data()
