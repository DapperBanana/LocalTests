
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['mycollection']

# Create
data = {'name': 'Alice', 'age': 30}
collection.insert_one(data)

# Read
result = collection.find_one({'name': 'Alice'})
print(result)

# Update
new_data = {'$set': {'age': 35}}
collection.update_one({'name': 'Alice'}, new_data)

# Read updated data
result_updated = collection.find_one({'name': 'Alice'})
print(result_updated)

# Delete
collection.delete_one({'name': 'Alice'})

# Verify delete operation
result_deleted = collection.find_one({'name': 'Alice'})
print(result_deleted)  # Should be None
