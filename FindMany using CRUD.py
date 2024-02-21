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

    # Define query criteria for finding documents
    documents_to_find = {"price": {"$gt": 300000}}

    # Find documents in the 'listings' collection that match the query criteria
    cursor = listings_collection.find(documents_to_find)

    # Initialize a counter to keep track of the number of documents found
    num_docs = 0

    # Iterate over the cursor to print each document and increment the counter
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
