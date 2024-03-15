//Database Schema Design and Setup:
 //We designed the database schema to accommodate employee, department, and project data, ensuring flexibility and scalability.
 //Below is a JSON representation of our MongoDB schema:

 {
   "employee": {
     "_id": ObjectId,
     "name": String,
     "email": String,
     "department_id": ObjectId,
     "project_ids": [ObjectId]
   },
   "department": {
     "_id": ObjectId,
     "name": String,
     "location": String
   },
   "project": {
     "_id": ObjectId,
     "name": String,
     "description": String,
     "department_id": ObjectId
   }
 }
