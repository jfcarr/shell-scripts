#!/usr/bin/env python

import os
import sys
import subprocess

def RunIt(cmdLine):
	with open(os.devnull, "w") as fnull:
		subprocess.call(cmdLine, stderr = fnull, shell=True)

### MAIN ###
try:
	if not len(sys.argv) == 2:
		print "Usage:"
		print "  xmlformat <input_file>"
	else:
		cmdTarget = sys.argv[1]

		RunIt("/usr/bin/xmlstarlet fo -t " + cmdTarget)

except Exception as ex:
	print "[ERROR] " + str(ex)
