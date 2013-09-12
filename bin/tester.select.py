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

open_orders = datastore.get_orders( {"status": [0]} )
#print open_orders
for row in open_orders:
	#print "%s will %s %s (bestellt %s)" % (row[1], row[3], row[2], time.ctime(row[5]))
        print "%s will %s %s (bestellt um %s), ID=%s, status=%s (%s)" % (row[1], row[3], row[2], time.strftime("%H:%M Uhr am %d.%m.%Y", time.localtime(row[5])), row[0], row[4], datastore.get_status(row[4]))
