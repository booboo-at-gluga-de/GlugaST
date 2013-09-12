#!/usr/bin/python

import sys, sqlite3, time
dbfile = "/var/websites/data/GulgaST.sqlite3.db"

#             0              1             2          3
status = ("bestellt", "ausgeliefert", "erhalten", "bezahlt")

def get_status(status_id):
	return status[status_id]

def db_initialize():
	print "initalizing database in %s" % dbfile

	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		db.execute('''CREATE TABLE orders (id INTEGER PRIMARY KEY, name text, item text, amount int, status int, timestamp int)''')
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
	now = int(time.time())

	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		db.execute("INSERT INTO orders(name, item, amount, status, timestamp) VALUES (?, ?, ?, 0, ?)", (name, item, amount, now))
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

def update_order_status(id, new_status):
	print "order %s gets new status %s" % (id, new_status)

	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		db.execute("UPDATE orders set status=%s where id=%s" % (new_status, id))
		conn.commit()
		conn.close()
		return(0)
	except sqlite3.OperationalError, ex:
		print "Not successful!!"
		print "OperationalError: %s" % ex
		return(1)
	except:
		raise
		print "Not successful!"
		return(1)


def get_orders( filter = {} ):
	print "getting orders with filter: %s" % filter
        sql = "SELECT * FROM orders"

	try:
            print 'filter["status"]: %s' % filter["status"]
            sql += " where status=%s" % filter["status"][0]
        except KeyError, ex:
            print 'ohne filter'
        except:
            raise

        print "SQL: %s" % sql

	try:
		# connection
		conn = sqlite3.connect(dbfile)
		# cursor
		db = conn.cursor()
		# return object is a list
		open_orders = []

		for row in db.execute(sql):
			open_orders.append(row)
			# print row
			# print "%s will %s %s" % (row[1], row[3], row[2])
		conn.close()
		return(open_orders)
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
