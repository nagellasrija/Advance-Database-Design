# Import necessary modules
from pymongo import MongoClient
import datetime
from pprint import pprint

# Define the MongoDB connection URI
uri = "mongodb+srv://nagellasrija:Srija@10@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

try:
    # Get reference to 'real_estate' database
    db = client.real_estate

    # Get reference to 'listings' collection
    listings_collection = db.listings

    # Define a document to be inserted into the 'listings' collection
    new_listing = {
        "property_type": "House",
        "location": "123 Main St, Cityville",
        "price": 350000,
        "bedrooms": 3,
        "bathrooms": 2,
        "square_feet": 2000,
        "built_year": 1995,
        "listing_date": datetime.datetime.utcnow(),
        "last_updated": datetime.datetime.utcnow()
    }

    # Insert the 'new_listing' document into the 'listings' collection
    result = listings_collection.insert_one(new_listing)

    # Retrieve the ID of the inserted document
    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
