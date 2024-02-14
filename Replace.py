from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# Define the MongoDB connection URI
uri = "mongodb+srv://nagellasrija:Srija@10@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.bank

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # Filter for the document to be replaced
    document_to_replace = {"_id": ObjectId("65c3ccf79cc8037988860049")}

    # Replacement document
    replacement_document = {
        "name": "Updated Name",
        "age": 30,
        "city": "Updated City"
    }

    # Print the original document
    pprint.pprint(accounts_collection.find_one(document_to_replace))

    # Replace the document with the specified replacement
    result = accounts_collection.replace_one(document_to_replace, replacement_document)

    # Print the number of documents replaced
    print("Documents replaced: " + str(result.modified_count))

    # Print the updated document
    pprint.pprint(accounts_collection.find_one(document_to_replace))

except Exception as e:
    print(e)
finally:
    client.close()
