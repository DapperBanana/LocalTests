
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['mycollection']

# Create operation
data = {'name': 'Alice', 'age': 25, 'country': 'USA'}
result = collection.insert_one(data)
print('Record inserted with id:', result.inserted_id)

# Read operation
query = {'name': 'Alice'}
result = collection.find_one(query)
print('Record found:', result)

# Update operation
update_query = {'name': 'Alice'}
new_data = {'$set': {'age': 26}}
collection.update_one(update_query, new_data)
print('Record updated')

# Read operation after update
result = collection.find_one(query)
print('Updated Record:', result)

# Delete operation
delete_query = {'name': 'Alice'}
collection.delete_one(delete_query)
print('Record deleted')

# Read operation after delete
result = collection.find_one(query)
print('Record after delete:', result)
