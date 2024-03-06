@@ -0,0 +1,16 @@
db.zips.aggregate([
  {
		$group:{
					_id: "$state",
					total_pop: { $sum:"$pop"}
        }
  },
  {
		$match: {
				totla_pop:{$lt:1000000}
			}
		},
  {
			$out: "small_states"
}
])
  60 changes: 60 additions & 0 deletions 60  
out.py
