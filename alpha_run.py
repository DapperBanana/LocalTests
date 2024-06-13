
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create operation
def create_document(data):
    collection.insert_one(data)
    print("Document created.")

# Read operation
def read_documents():
    documents = collection.find()
    for document in documents:
        print(document)

# Update operation
def update_document(query, new_data):
    collection.update_one(query, {"$set": new_data})
    print("Document updated.")

# Delete operation
def delete_document(query):
    collection.delete_one(query)
    print("Document deleted.")

# Usage
data = {"name": "John", "age": 30, "city": "New York"}

# Create
create_document(data)

# Read
print("All documents:")
read_documents()

# Update
update_query = {"name": "John"}
new_data = {"$set": {"age": 35}}
update_document(update_query, new_data)

# Read updated document
print("After update:")
read_documents()

# Delete
delete_query = {"name": "John"}
delete_document(delete_query)

# Read remaining documents
print("After delete:")
read_documents()
