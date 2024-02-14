// Find all documents in the 'birds' collection where the 'conservationStatus' field is set to "Least Concern"
 db.birds.find({conservationStatus:"Least Concern"})
// Delete all documents from the 'birds' collection where the 'conservationStatus' field is set to "Least Concern"
 db.birds.deleteMany({conservationStatus:"Least Concern"})
