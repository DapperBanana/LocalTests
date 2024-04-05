
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

# Create
def create_document(collection, data):
    result = collection.insert_one(data)
    print('Document inserted with ID:', result.inserted_id)

# Read
def read_documents(collection, query={}):
    results = collection.find(query)
    for result in results:
        print(result)

# Update
def update_document(collection, query, new_data):
    result = collection.update_one(query, {'$set': new_data})
    print(result.modified_count, 'document updated.')

# Delete
def delete_document(collection, query):
    result = collection.delete_one(query)
    print(result.deleted_count, 'document deleted.')

# Sample data
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Perform CRUD operations
collection = db['mycollection']

create_document(collection, data)
read_documents(collection)
update_document(collection, {'name': 'John'}, {'age': 35})
read_documents(collection)
delete_document(collection, {'name': 'John'})
read_documents(collection)
