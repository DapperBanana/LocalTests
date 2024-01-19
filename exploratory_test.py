
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Create operation
def create_document():
    document = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    result = collection.insert_one(document)
    print(f"Document created with id: {result.inserted_id}")

# Read operation
def get_documents():
    documents = collection.find()
    for document in documents:
        print(document)

# Update operation
def update_document():
    filter = {'name': 'John Doe'}
    update = {'$set': {'age': 35}}
    result = collection.update_one(filter, update)
    print(f"{result.modified_count} document updated")

# Delete operation
def delete_document():
    filter = {'name': 'John Doe'}
    result = collection.delete_one(filter)
    print(f"{result.deleted_count} document deleted")

# Call the functions
create_document()
get_documents()
update_document()
get_documents()
delete_document()
get_documents()
