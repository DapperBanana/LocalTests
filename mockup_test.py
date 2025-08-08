
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Insert a document
data1 = {'name': 'John', 'age': 30, 'city': 'New York'}
data2 = {'name': 'Alice', 'age': 25, 'city': 'San Francisco'}

result = collection.insert_one(data1)
print('Document inserted with id:', result.inserted_id)

result = collection.insert_one(data2)
print('Document inserted with id:', result.inserted_id)

# Find documents
query = {'city': 'New York'}
results = collection.find(query)

for result in results:
    print(result)

# Update a document
query = {'name': 'John'}
new_data = {'$set': {'age': 32}}
result = collection.update_one(query, new_data)
print('Document updated:', result.modified_count)

# Delete a document
query = {'name': 'Alice'}
result = collection.delete_one(query)
print('Document deleted:', result.deleted_count)

# Drop the collection
collection.drop()
