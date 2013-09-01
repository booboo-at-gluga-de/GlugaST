#!/usr/bin/python

import sys, os
home=os.environ.get("HOME")
sys.path.append(home + "/git/GlugaST/lib/")
import datastore

#print sys.path

#datastore.db_initialize()

#print "len argv: %s" % len(sys.argv)
#print "argv: %s" % sys.argv[1]

if len(sys.argv) < 4:
	print "not enough arguments"
	print "call using"
	print ""
	print "%s <name> <item> <amount>" % sys.argv[0]
	print ""
	print "where"
	print "<name>   is the name of the person ordering"
	print "<item>   describes what is ordered"
	print "<amount> is an integer telling how much is ordered"
	exit(1)

datastore.add_order(sys.argv[1], sys.argv[2], sys.argv[3])
