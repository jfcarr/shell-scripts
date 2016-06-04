#!/usr/bin/env python

import json
import sys

try:
	if not len(sys.argv) == 2:
		print "Usage:"
		print "  jsonvalid <input_file>"
	else:
		json_data = open(sys.argv[1])
		data = json.load(json_data)
		
		print sys.argv[1] + ' is OK'

except Exception, err:
	print str(err)
