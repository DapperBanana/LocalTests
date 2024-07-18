letion(id='chatcmpl-9mA1A3Kb89823J2NsJOyy3H35an2m', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import sqlite3

# Connect to the database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             name TEXT,
             email TEXT)''')

def create_user(name, email):
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

def read_all_users():
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    for row in rows:
        print(row)

def read_user(user_id):
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = c.fetchone()
    print(row)

def update_user(user_id, name, email):
    c.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, user_id))
    conn.commit()

def delete_user(user_id):
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()

# Create a user
create_user("Alice", "alice@example.com")

# Read all users
read_all_users()

# Read user by id
read_user(1)

# Update user
update_user(1, "Alice Smith", "alice.smith@example.com")

# Delete user
delete_user(1)

conn.close()', role='assistant', function_call=None, tool_calls=None))], created=1721265280, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=274, prompt_tokens=21, total_tokens=295)