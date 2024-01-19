
import sqlite3

# Function to create a new record
def create_record(connection, cursor, record):
    cursor.execute("INSERT INTO records (name, age) VALUES (?, ?)", (record['name'], record['age']))
    connection.commit()
    print("Record created successfully")

# Function to read all records
def read_records(connection, cursor):
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Age:", row[2])

# Function to update a record
def update_record(connection, cursor, record):
    cursor.execute("UPDATE records SET age = ? WHERE id = ?", (record['age'], record['id']))
    connection.commit()
    print("Record updated successfully")

# Function to delete a record
def delete_record(connection, cursor, record_id):
    cursor.execute("DELETE FROM records WHERE id = ?", (record_id,))
    connection.commit()
    print("Record deleted successfully")

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS records
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   age INTEGER NOT NULL)''')

while True:
    print("\n1. Create record")
    print("2. Read all records")
    print("3. Update record")
    print("4. Delete record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        record = {'name': name, 'age': age}
        create_record(conn, cursor, record)

    elif choice == '2':
        read_records(conn, cursor)

    elif choice == '3':
        record_id = int(input("Enter record ID: "))
        age = int(input("Enter new age: "))
        record = {'id': record_id, 'age': age}
        update_record(conn, cursor, record)

    elif choice == '4':
        record_id = int(input("Enter record ID: "))
        delete_record(conn, cursor, record_id)

    elif choice == '5':
        break

    else:
        print("Invalid choice")

# Close the connection to the database
conn.close()
