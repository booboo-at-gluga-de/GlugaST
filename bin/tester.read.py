#!/usr/bin/python

import sys, os, time
home=os.environ.get("HOME")
sys.path.append(home + "/git/GlugaST/lib/")
import datastore

#print sys.path

#datastore.db_initialize()

#print "len argv: %s" % len(sys.argv)
#print "argv: %s" % sys.argv[1]

#if len(sys.argv) < 4:
#	print "not enough arguments"
#	exit(1)

open_orders = datastore.get_orders()
print open_orders
for row in open_orders:
	print "%s will %s %s (bestellt %s)" % (row[1], row[3], row[2], time.ctime(row[5]))
	print "(bestellt %s)" % time.localtime(row[5])
