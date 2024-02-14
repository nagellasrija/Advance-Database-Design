# Import necessary modules
 from pymongo.mongo_client import MongoClient
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

     # Filter
     document_to_update = {"_id": ObjectId("65c3ccf79cc8037988860049")}

     # Update
     add_to_balance = {"$inc": {"balance": 100}}

     # Print original document
     pprint.pprint(accounts_collection.find_one(document_to_update))

    # Update the document with the specified operation
     result = accounts_collection.update_one(document_to_update, add_to_balance)

    # Print the number of documents updated
     print("Documents updated: " + str(result.modified_count))

     # Print updated document
     pprint.pprint(accounts_collection.find_one(document_to_update))


 except Exception as e:
     print(e)
 finally:
     client.close()
