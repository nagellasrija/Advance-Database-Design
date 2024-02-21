# Import necessary modules
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

    # Get reference to 'real_estate' database
    db = client.real_estate

    # Get reference to 'listings' collection
    listings_collection = db.listings

    # Define filter criteria for the documents to delete
    documents_to_delete = {"bedrooms": {"$lt": 2}}

    # Search for sample document before delete
    print("Searching for sample target documents before delete: ")
    for document in listings_collection.find(documents_to_delete):
        pprint.pprint(document)

    # Delete the documents
    result = listings_collection.delete_many(documents_to_delete)

    # Search for sample document after delete
    print("Searching for sample target documents after delete: ")
    for document in listings_collection.find(documents_to_delete):
        pprint.pprint(document)

    # Print the number of documents deleted
    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
