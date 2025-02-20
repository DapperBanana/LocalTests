
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('test.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS employees 
             (id INTEGER PRIMARY KEY, name TEXT, salary REAL)''')

# Create
def create_employee(id, name, salary):
    c.execute("INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)", (id, name, salary))
    conn.commit()
    print("Employee created successfully")

# Read
def read_employee(id):
    c.execute("SELECT * FROM employees WHERE id=?", (id,))
    employee = c.fetchone()
    if employee:
        print("Employee ID:", employee[0])
        print("Employee name:", employee[1])
        print("Employee salary:", employee[2])
    else:
        print("Employee not found")

# Update
def update_employee(id, name, salary):
    c.execute("UPDATE employees SET name=?, salary=? WHERE id=?", (name, salary, id))
    conn.commit()
    print("Employee updated successfully")

# Delete
def delete_employee(id):
    c.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    print("Employee deleted successfully")

# Perform CRUD operations
create_employee(1, 'Alice', 50000)
read_employee(1)
update_employee(1, 'Alice Smith', 60000)
delete_employee(1)

# Close connection
conn.close()
