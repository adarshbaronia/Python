import db


#db.add_one('saggy', 'Leon', 'leon@xyz.com')

# to delete record use str rowid 
#db.del_one(str(7))

#add many records
stuff = [
		('Bruce','Admin','admin@gmail.com'),
		('Corey','Anderson','corey@codemy.com')
]

#db.add_many(stuff)

db.lookup_email('dan@fcc.com')

#db.show_all()
