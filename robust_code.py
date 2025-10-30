
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Create
def create_document(data):
    collection.insert_one(data)

# Read
def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

# Update
def update_document(query, new_data):
    collection.update_one(query, {'$set': new_data})

# Delete
def delete_document(query):
    collection.delete_one(query)

# Example usage
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

create_document(data)
read_documents()

update_query = {'name': 'John Doe'}
update_data = {'age': 35}
update_document(update_query, update_data)
read_documents()

delete_query = {'name': 'John Doe'}
delete_document(delete_query)
read_documents()

client.close()
