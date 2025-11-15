
from pymongo import MongoClient

# Connect to the MongoDB database
client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_collection']

# Create
new_document = {'name': 'Alice', 'age': 30, 'city': 'New York'}
insert_result = collection.insert_one(new_document)
print(f'Inserted document id: {insert_result.inserted_id}')

# Read
results = collection.find({'name': 'Alice'})
for result in results:
    print(result)

document_to_update = collection.find_one({'name': 'Alice'})
# Update
collection.update_one({'_id': document_to_update['_id']}, {'$set': {'age': 31}})
updated_document = collection.find_one({'name': 'Alice'})
print(f'Updated document: {updated_document}')

# Delete
delete_result = collection.delete_one({'name': 'Alice'})
print(f'Deleted document: {delete_result.deleted_count}')

# Close the connection
client.close()
