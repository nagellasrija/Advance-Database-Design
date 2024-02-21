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

    # Define filter criteria for the document to delete
    document_to_delete = {"_id": ObjectId("65c3ccf79cc8037988860048")}

    # Search for document before delete
    print("Searching for target document before delete: ")
    pprint.pprint(listings_collection.find_one(document_to_delete))

    # Delete the document
    result = listings_collection.delete_one(document_to_delete)

    # Search for document after delete
    print("Searching for target document after delete: ")
    pprint.pprint(listings_collection.find_one(document_to_delete))

    # Print the number of documents deleted
    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
