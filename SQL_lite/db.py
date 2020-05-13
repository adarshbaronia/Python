import sqlite3

# to create a connectionn in the memory
# conn * sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()
# select function
def show_all():
	c.execute("SELECT rowid, * FROM customers")
	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()
	#close connction
	conn.close()

# add function
def add_one(first, last, email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

	conn.commit()
	#close connction
	conn.close()

#delete record

def del_one(id):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("DELETE FROM customers WHERE rowid = (?)", id)

	conn.commit()
	#close connction
	conn.close()


def add_many(list):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

	conn.commit()
	#close connction
	conn.close()



#where clause

def lookup_email(email):
	conn = sqlite3.connect('customer.db')
	c = conn.cursor()
	c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))
	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()
	#close connction
	conn.close()


