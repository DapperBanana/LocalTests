
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Create
def create_document(collection, data):
    db[collection].insert_one(data)

# Read
def read_documents(collection, query=None):
    if query:
        documents = db[collection].find(query)
    else:
        documents = db[collection].find()
    
    for document in documents:
        print(document)

# Update
def update_document(collection, query, new_data):
    db[collection].update_one(query, {"$set": new_data})

# Delete
def delete_document(collection, query):
    db[collection].delete_one(query)

# Example usage
# Create a new document
data = {"name": "John", "age": 30}
create_document("users", data)

# Read documents
read_documents("users")

# Update a document
update_query = {"name": "John"}
new_data = {"name": "John Doe", "age": 35}
update_document("users", update_query, new_data)

# Delete a document
delete_query = {"name": "John Doe"}
delete_document("users", delete_query)

# Read documents after update and delete
read_documents("users")
