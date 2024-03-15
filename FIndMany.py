from pymongo.server_api import ServerApi
 import pprint


 uri = "mongodb+srv://nagellasrija:Srija@10@cluster0.4xuta2y.mongodb.net/"


 # Create a new client and connect to the server
 client = MongoClient(uri, server_api=ServerApi('1'))


 try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')


    # Get reference to 'ompany_management' database
    db = client.company_management


    # Get reference to 'employees' collection
    accounts_collection = db.employees


    # Find documents matching a query
    query = {"account_type": "savings"}
    results = accounts_collection.find(query)


    # Print the results
    print("Documents with account_type as savings:")
    for document in results:
        pprint.pprint(document)


 except Exception as e:
    print(e)
 finally:
    client.close()
