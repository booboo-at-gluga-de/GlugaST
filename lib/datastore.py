#!/usr/bin/python

import sys, os, sqlite3
home=os.environ.get("HOME")
dbfile = home + "/git/GlugaST/data/GulgaST.sqlite3.db"

#             0              1             2          3
status = ("bestellt", "ausgeliefert", "erhalten", "bezahlt")


def db_initialize():
	print "initalizing database in %s" % dbfile

	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		db.execute('''CREATE TABLE orders (id INTEGER PRIMARY KEY, name text, item text, amount int, status int)''')
		conn.commit()
		conn.close()
		return(0)
	except sqlite3.OperationalError, ex:
		print "Not successful!!"
		print "OperationalError: %s" % ex
		return(1)
	except:
		print "Not successful, error unknown!"
		return(1)


def add_order(name, item, amount):
	amount=int(amount)
	print "adding order: %s orders %s %s" % (name, amount, item)

	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		db.execute("INSERT INTO orders(name, item, amount, status) VALUES (?, ?, ?, 0)", (name, amount, item))
		conn.commit()
		conn.close()
		return(0)
	except sqlite3.OperationalError, ex:
		print "Not successful!!"
		print "OperationalError: %s" % ex
		return(1)
	except:
		print "Not successful, error unknown!"
		return(1)

def get_orders():
	print "getting orders"
	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		for row in db.execute("SELECT * FROM orders"):
			print row
			# print "%s will %s %s" % (row[1], row[3], row[2])
		conn.close()
		return(0)
	except sqlite3.OperationalError, ex:
		print "Not successful!!"
		print "OperationalError: %s" % ex
		return(1)
	except:
		print "Not successful, error unknown!"
		return(1)


# you may call
# datastore init
# to create a sqlite db

for arg in sys.argv:
	#print "arg: %s" % arg
	if arg == "init":
		rc=db_initialize()
		exit(rc)
