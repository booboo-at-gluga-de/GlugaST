#!/usr/bin/python

import sys, os
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

datastore.get_orders()
