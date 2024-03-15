from pymongo import MongoClient
 import datetime


 # MongoDB connection URI
 uri = "mongodb+srv://nagellasrija:Srija@10@cluster0.4xuta2y.mongodb.net/"


 # Create a new client and connect to the server
 client = MongoClient(uri)


 try:
    # Get reference to the 'company_management' database
    db = client.company_management


    # Get reference to the 'employees' collection
    employees_collection = db.employees


    # Inserting one employee
    new_employee = {
        "name": "John Doe",
        "position": "Software Engineer",
        "department": "Engineering",
        "salary": 75000,
        "hire_date": datetime.datetime.utcnow(),
    }


    # Write an expression that inserts the 'new_employee' document into the 'employees' collection.
    result = employees_collection.insert_one(new_employee)


    # Retrieve the _id of the inserted document
    employee_id = result.inserted_id
    print(f"_id of inserted employee: {employee_id}")


 except Exception as e:
    print(e)
 finally:
    client.close()
