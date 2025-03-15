
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_db.db')
cur = conn.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS contacts
               (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')

def create_contact(name, phone):
    cur.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    print("Contact created successfully")

def read_contacts():
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    for contact in contacts:
        print(contact)

def update_contact(contact_id, new_name, new_phone):
    cur.execute("UPDATE contacts SET name = ?, phone = ? WHERE id = ?", (new_name, new_phone, contact_id))
    conn.commit()
    print("Contact updated successfully")

def delete_contact(contact_id):
    cur.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print("Contact deleted successfully")

# Main program
create_contact("John Doe", "123-456-7890")
create_contact("Jane Smith", "987-654-3210")
read_contacts()
update_contact(1, "John Doe Jr.", "999-999-9999")
delete_contact(2)
read_contacts()

# Close the database connection
conn.close()
