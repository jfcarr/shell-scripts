#!/usr/bin/env python

import xml.etree.ElementTree as ET
import sys

try:
	if not len(sys.argv) == 2:
		print "Usage:"
		print "  xmlvalid <input_file>"
	else:
		tree = ET.parse(sys.argv[1])
		root = tree.getroot()
		print sys.argv[1] + ' is OK'

except Exception, err:
	print str(err)
