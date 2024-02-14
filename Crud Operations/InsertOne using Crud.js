# Import necessary modules
from pymongo.mongo_client import MongoClient
 from pymongo.server_api import ServerApi
 import datetime
 from pprint import pprint
  
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

    # Define a document to be inserted into the 'accounts' collection
     new_account = {
         "account_holder": "Linus Torvalds",
         "account_id": "MDB829001337",
         "account_type": "checking",
         "balance": 50352434,
         "last_updated": datetime.datetime.utcnow(),
     }

    # Insert the 'new_account' document into the 'accounts' collection
     result = accounts_collection.insert_one(new_account)
    # Retrieve the ID of the inserted document
     document_id = result.inserted_id
     pprint(f"_id of inserted document: {document_id}")


 except Exception as e:
    # Print any exceptions that occur
     print(e)
 finally:
    # Close the MongoClient to release resources
     client.close()
