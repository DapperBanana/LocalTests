
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Create operation
def create_document(data):
    result = collection.insert_one(data)
    print("Document created with id:", result.inserted_id)

# Read operation
def read_documents():
    for doc in collection.find():
        print(doc)

# Update operation
def update_document(query, new_data):
    result = collection.update_one(query, {"$set": new_data})
    print("Document updated:", result.modified_count)

# Delete operation
def delete_document(query):
    result = collection.delete_one(query)
    print("Document deleted:", result.deleted_count)

# Example usage
data = {"name": "John", "age": 30, "city": "New York"}
create_document(data)

read_documents()

update_query = {"name": "John"}
new_data = {"age": 35, "city": "San Francisco"}
update_document(update_query, new_data)

delete_query = {"name": "John"}
delete_document(delete_query)

read_documents()

# Close connection
client.close()
