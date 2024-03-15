 from pymongo import MongoClient
 from pymongo.server_api import ServerApi
 from pymongo import UpdateOne
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


    # Data entries to insert
    data_entries = [
        {"account_holder": "Sathvik Putta", "account_type": "savings", "balance": 5000},
        {"account_holder": "Tejagni Chichili", "account_type": "checking", "balance": 7000},
        {"account_holder": "Srija", "account_type": "savings", "balance": 3000},
        {"account_holder": "Vidya", "account_type": "checking", "balance": 6000},
        {"account_holder": "Kaushik", "account_type": "savings", "balance": 4000},
        {"account_holder": "Yathisha", "account_type": "checking", "balance": 8000},
        {"account_holder": "Ravi shankar", "account_type": "savings", "balance": 5500},
        {"account_holder": "Nandini", "account_type": "checking", "balance": 7500},
        {"account_holder": "Tejasri", "account_type": "savings", "balance": 4800},
        {"account_holder": "Pooja", "account_type": "checking", "balance": 8200},
        {"account_holder": "Arunitha", "account_type": "savings", "balance": 6200},
        {"account_holder": "Vikky", "account_type": "checking", "balance": 5400},
        {"account_holder": "Mukesh", "account_type": "savings", "balance": 7300},
        {"account_holder": "Chandra", "account_type": "checking", "balance": 6800},
        {"account_holder": "Lochan", "account_type": "savings", "balance": 4800},
        {"account_holder": "Dinesh", "account_type": "checking", "balance": 7200},
        {"account_holder": "Karthik", "account_type": "savings", "balance": 6100},
        {"account_holder": "Geetha", "account_type": "checking", "balance": 5600},
        {"account_holder": "Ramya", "account_type": "savings", "balance": 6900},
        {"account_holder": "Sravan", "account_type": "checking", "balance": 7700}
    ]


    # Insert multiple data entries into the 'accounts' collection.
    result = accounts_collection.insert_many(data_entries)


    # Print the inserted document IDs
    pprint.pprint(result.inserted_ids)


    # Update a document
    update_query = {"account_holder": "Sathvik Putta"}
    update_data = {"$set": {"balance": 16000}}
    update_operation = UpdateOne(update_query, update_data)
    update_result = accounts_collection.bulk_write([update_operation])


    # Print the output of the update operation
    pprint.pprint(update_result.bulk_api_result)


 except Exception as e:
    print(e)
 finally:
    client.close()
