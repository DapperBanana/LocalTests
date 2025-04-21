
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['mycollection']

# Create
data = {'name': 'John', 'age': 30, 'city': 'New York'}
result = collection.insert_one(data)
print('Inserted document with ID:', result.inserted_id)

# Read
result = collection.find_one({'name': 'John'})
print('Retrieved document:', result)

# Update
update_data = {'$set': {'age': 31}}
result = collection.update_one({'name': 'John'}, update_data)
print('Updated document count:', result.modified_count)

# Delete
result = collection.delete_one({'name': 'John'})
print('Deleted document count:', result.deleted_count)
