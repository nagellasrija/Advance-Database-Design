// Find the document with the title "The MongoDB Podcast"
 db.podcasts.findOne({title: "The MongoDB Podcast"});
// Find the document with the specified ObjectId
 db.podcasts.findOne({_id: ObjectId("6261a92dfee1ff300dc80bf1")});
// Set the subscribers field to 98562 for the document with the specified ObjectId
 db.podcasts.updateOne({_id: ObjectId("6261a92dfee1ff300dc80bf1")},{$set:{subscribers:98562}})
