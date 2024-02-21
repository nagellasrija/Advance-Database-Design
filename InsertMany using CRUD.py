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

    # Define multiple documents to be inserted into the 'listings' collection
    new_listings = [
        {
            "property_type": "House",
            "location": "123 Main St, Cityville",
            "price": 350000,
            "bedrooms": 3,
            "bathrooms": 2,
            "square_feet": 2000,
            "built_year": 1995,
            "listing_date": datetime.datetime.utcnow(),
            "last_updated": datetime.datetime.utcnow()
        },
        {
            "property_type": "Condo",
            "location": "456 Elm St, Townsville",
            "price": 250000,
            "bedrooms": 2,
            "bathrooms": 1,
            "square_feet": 1200,
            "built_year": 2005,
            "listing_date": datetime.datetime.utcnow(),
            "last_updated": datetime.datetime.utcnow()
        }
    ]

    # Insert the 'new_listings' documents into the 'listings' collection
    result = listings_collection.insert_many(new_listings)

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
