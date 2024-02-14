# Import necessary modules
 from pymongo.mongo_client import MongoClient
 from pymongo.server_api import ServerApi
 import datetime
   
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

     # inserting many accounts
     new_accounts = [
         {
             "account_id": "MDB011235813",
             "account_holder": "Ada Lovelace",
             "account_type": "checking",
             "balance": 60218,
         },
         {
             "account_id": "MDB829000001",
             "account_holder": "Muhammad ibn Musa al-Khwarizmi",
             "account_type": "savings",
             "balance": 267914296,
         },
     ]

    # Insert the 'new_accounts' documents into the 'accounts' collection
     result = accounts_collection.insert_many(new_accounts)

    # Retrieve the IDs of the inserted documents
     document_ids = result.inserted_ids
     print("# of documents inserted: " + str(len(document_ids)))
     print(f"_ids of inserted documents: {document_ids}")


 except Exception as e:
    # Print any exceptions that occur
     print(e)
 finally:
    # Close the MongoClient to release resources
     client.close()
