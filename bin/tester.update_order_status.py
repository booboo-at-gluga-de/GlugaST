#!/usr/bin/python

import sys, os
home=os.environ.get("HOME")
sys.path.append(home + "/git/GlugaST/lib/")
import datastore

#print sys.path

#datastore.db_initialize()

#print "len argv: %s" % len(sys.argv)
#print "argv: %s" % sys.argv[1]

if len(sys.argv) < 3:
	print "not enough arguments"
	print "call using"
	print ""
	print "%s <id> <new_state>" % sys.argv[0]
	print ""
	print "where"
	print "<id>   is the id of the order you want to update"
	print "<new_state>   is the numerical representation of the new state"
	exit(1)

datastore.update_order_status(sys.argv[1], sys.argv[2])
