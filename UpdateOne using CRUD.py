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

    # Define filter criteria for the document to update
    document_to_update = {"_id": ObjectId("65c3ccf79cc8037988860049")}

    # Define the update operation
    update_operation = {"$set": {"price": 375000}}

    # Print original document
    pprint.pprint(listings_collection.find_one(document_to_update))

    # Update the document with the specified operation
    result = listings_collection.update_one(document_to_update, update_operation)

    # Print the number of documents updated
    print("Documents updated: " + str(result.modified_count))

    # Print updated document
    pprint.pprint(listings_collection.find_one(document_to_update))

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
