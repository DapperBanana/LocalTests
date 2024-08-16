
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Create
def create_document(collection, data):
    return collection.insert_one(data)

# Read
def read_documents(collection, query={}):
    return collection.find(query)

# Update
def update_document(collection, query, new_data):
    return collection.update_one(query, {"$set": new_data})

# Delete
def delete_document(collection, query):
    return collection.delete_one(query)

# Example usage
collection = db["customers"]

# Create a new document
data = { "name": "John", "address": "Highway 37" }
document_id = create_document(collection, data)

# Read all documents
for document in read_documents(collection):
    print(document)

# Update a document
update_data = { "address": "Ocean View 2" }
query = { "name": "John" }
update_document(collection, query, update_data)

# Delete a document
delete_document(collection, query)

# Read all documents after delete
for document in read_documents(collection):
    print(document)
