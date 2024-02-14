// Update the document with the title "The Developer Hub", adding the topics field if it doesn't exist, or updating it with the specified array of topics
db.podcasts.updateOne(
   {title: "The Developer Hub"},
   {$set: {topics: ["databases", "MongoDB"]}}
 );
// Confirm the update by finding the document with the title "The Developer Hub"
 db.podcasts.findOne({title: "The Developer Hub"});
