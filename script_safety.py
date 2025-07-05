
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Create - Insert a document
document = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
result = collection.insert_one(document)
print(f'Inserted document with ID: {result.inserted_id}')

# Read - Find documents
query = {'name': 'Alice'}
result = collection.find_one(query)
print(f'Retrieved document: {result}')

# Update - Update a document
update_query = {'name': 'Alice'}
new_values = {'$set': {'city': 'San Francisco'}}
collection.update_one(update_query, new_values)
updated_result = collection.find_one({'name': 'Alice'})
print(f'Updated document: {updated_result}')

# Delete - Delete a document
delete_query = {'name': 'Alice'}
collection.delete_one(delete_query)
deleted_result = collection.find_one({'name': 'Alice'})
print(f'Deleted document: {deleted_result}')
