// Find documents in the 'listingsAndReviews' collection where the 'bed_type' field is "Real Bed" and sort the results in ascending order based on the 'name' field
  db.listingsAndReviews.find({bed_type: "Real Bed"}).sort({name: 1});
 // Find documents in the 'listingsAndReviews' collection where the 'bed_type' field is "Real Bed" and sort the results in descending order based on the 'name' field
  db.listingsAndReviews.find({bed_type: "Real Bed"}).sort({name: -1});

 // Find documents in the 'listingsAndReviews' collection where the 'bed_type' field is "Real Bed", project only the 'name' field, and sort the results in ascending order based on the 'name' field
  db.listingsAndReviews.find({bed_type: "Real Bed"}, {name: 1}).sort({name: 1});
 // Find documents in the 'listingsAndReviews' collection where the 'bed_type' field is "Real Bed", project only the 'name' field, and sort the results in descending order based on the 'name' field
  db.listingsAndReviews.find({bed_type: "Real Bed"}, {name: -1}).sort({name: -1});

 // Find documents in the 'listingsAndReviews' collection where the 'bed_type' field is "Real Bed" and the 'property_type' field is "Apartment", sort the results in descending order based on the 'name' field, and limit the results to 3
  db.listingsAndReviews
    .find({bed_type: "Real Bed"}, {property_type: "Apartment"})
    .sort({name: -1})
    .limit(3);
