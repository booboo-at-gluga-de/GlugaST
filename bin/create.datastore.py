#!/usr/bin/python

import sys, os
home=os.environ.get("HOME")
sys.path.append(home + "/git/GlugaST/lib/")
import datastore

datastore.db_initialize()
