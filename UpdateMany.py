 from pymongo import MongoClient
 from pymongo.server_api import ServerApi
 import pprint


 uri = "mongodb+srv://nagellasrija:Srija@10@cluster0.4xuta2y.mongodb.net/"


 # Create a new client and connect to the server
 client = MongoClient(uri, server_api=ServerApi('1'))


 try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')


    # Get reference to 'company_management' database
    db = client.company_management


    # Get reference to 'employees' collection
    accounts_collection = db.employees


    # Perform update_many operation
    filter_query = {"account_type": "savings"}  # Filter criteria
    update_query = {"$set": {"balance": 6000}}  # Update criteria


    # Execute the update_many operation
    result = accounts_collection.update_many(filter_query, update_query)


    # Print out the details of the update
    print("Number of documents matched:", result.matched_count)
    print("Number of documents modified:", result.modified_count)


 except Exception as e:
    print(e)
 finally:
    client.close()
