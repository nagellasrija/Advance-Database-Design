// Find a restaurant in the 'restaurants' collection where the 'borough' field is "Brooklyn"
 db.restaurants.findOne({borough: "Brooklyn"});
// Find a restaurant in the 'restaurants' collection where the 'borough' field is "Brooklyn", projecting only the 'cuisine' and 'zipcode' fields
 db.restaurants.findOne({borough: "Brooklyn"}, {cuisine: 1, zipcode: 1});
// Find a restaurant in the 'restaurants' collection where the 'borough' field is "Brooklyn", excluding the 'cuisine', 'zipcode', and '_id' fields
 db.restaurants.findOne({borough: "Brooklyn"}, {cuisine: 0, zipcode: 0, _id: 0});
// Find a restaurant in the 'restaurants' collection where the 'borough' field is "Brooklyn", projecting only the 'cuisine' and 'zipcode' fields, excluding the '_id' field
 db.restaurants.findOne({borough: "Brooklyn"}, {cuisine: 1, zipcode: 1, _id: 0});

// Switch to the 'training_sample' database to run the following queries
 db.inspections.find(
     { sector: "Restaurant - 818" },
     { business_name: 1, result: 1, _id: 0 }
   )

 db.inspections.find(
     { result: { $in: ["Pass", "Warning"] } },
     { date: 0, "address.zip": 0 }
 )
