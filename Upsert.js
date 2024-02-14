// Update the document with the title "The Developer Hub", setting the topics field to ["databases", "MongoDB"], and if the document does not exist, insert it.
db.podcasts.updateOne(
   {title: "The Developer Hub"},
   {$set: {topics: ["databases", "MongoDB"]}},
   {upsert:true}
 );
