
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Create
def create_document(data):
    result = collection.insert_one(data)
    print('Created document with id:', result.inserted_id)

# Read
def read_document(query):
    result = collection.find(query)
    for document in result:
        print(document)

# Update
def update_document(query, new_values):
    result = collection.update_many(query, new_values)
    print(result.modified_count, 'documents updated')

# Delete
def delete_document(query):
    result = collection.delete_many(query)
    print(result.deleted_count, 'documents deleted')

# Usage examples
data = {'name': 'John', 'age': 28, 'city': 'New York'}

create_document(data)
read_document({})
update_document({'name': 'John'}, {'$set': {'age': 30}})
delete_document({'name': 'John'})

client.close()
