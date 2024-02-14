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

      # inserting one account
      documents_to_find = {"balance": {"$gt": 4700}}

      # Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
      cursor = accounts_collection.find(documents_to_find)

      # Initialize a counter to keep track of the number of documents found
      num_docs = 0

     # Iterate over the cursor to print each document and increment the counter
      for document in cursor:
          num_docs += 1
          pprint.pprint(document)
          print()
      print("# of documents found: " + str(num_docs))


  except Exception as e:
      print(e)
  finally:
      client.close()