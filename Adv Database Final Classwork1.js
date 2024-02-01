//Query 1
// Create a collection named 'classwork'
db.createCollection('classwork')

// Insert a document into the 'classwork' collection
db.classwork.insertOne({
    "_id": 123,
    "Emp_ID": "10025AE336",
    "Personal_details": {
        "First_Name": "Radhika",
        "Last_Name": "Sharma",
        "Date_Of_Birth": "1995-09-26"
    },
    "Contact": {
        "e-mail": "radhika_sharma.123@gmail.com",
        "phone": "9848022338"
    },
    "Address": {
        "city": "Hyderabad",
        "Area": "Madapur",}})
/*OutPut:
{
  acknowledged: true,
  insertedId: 123
}*/

//Query 2
// Create the collection named 'School'
db.createCollection('School')
// Insert a document into the 'School' collection
db.School.insertOne([  
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  }

/* OutPut:
 {
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('65b1553c5326bc7c7f57cf1c')
    }
}*/


//Query 3
// Create a collection named 'Home'
db.createCollection('Home')
// Insert multiple documents into the 'Home' collection
db.Home.insertMany([  
  {
    title: "Post Title 2",
    body: "Body of post.",
    category: "Event",
    likes: 2,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 3",
    body: "Body of post.",
    category: "Technology",
    likes: 3,
    tags: ["news", "events"],
    date: Date()
  },
  {
    title: "Post Title 4",
    body: "Body of post.",
    category: "Event",
    likes: 4,
    tags: ["news", "events"],
    date: Date()
  }
])

/*OutPut:
    {
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('65b1553c5326bc7c7f57cf1c'),
    '1': ObjectId('65b1553c5326bc7c7f57cf1d'),
    '2': ObjectId('65b1553c5326bc7c7f57cf1e')
  }
}
*/
