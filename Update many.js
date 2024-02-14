// Update multiple documents in the 'books' collection where the 'publishedDate' is less than the specified date, setting the 'status' field to "NEW"
db.books.updateMany(
   {publishedDate: {$lt: ISODate("2017-04-27T08:00:00.000+00:00")}},
   {$set: {status: "NEW"}}
 );
