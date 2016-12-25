#!/usr/bin/python3

import subprocess

def GetInfo(address, port):
	allresults = []
	driveInfo = {"Path": "", "Name": "", "Value": 0, "Scale": "C"}
	callresult = subprocess.check_output(["netcat", address, port])
	callresult = callresult.decode("utf-8")  # convert byte array to string
	disks = callresult.split("||")
	
	for disk in disks:
		diskparts = disk.split("|")
		diskparts.remove("")
		
		driveInfo["Path"] = diskparts[0]
		driveInfo["Name"] = diskparts[1]
		driveInfo["Value"] = diskparts[2]
		driveInfo["Scale"] = diskparts[3]

		if driveInfo["Scale"] == "C":
			driveInfo["Value"] = (float(driveInfo["Value"]) * (9/5)) + 32
			driveInfo["Scale"] = "F"
		
		formattedInfo = driveInfo["Path"] + " is " + str(driveInfo["Value"]) + " " + driveInfo["Scale"]
		allresults.append(formattedInfo)
		
	return allresults

allresults = GetInfo("localhost", "7634")

loopIteration = 0
printResult = ""
for tempResult in allresults:
	if loopIteration > 0:
		printResult = printResult + ", "
	printResult = printResult + tempResult
	loopIteration = loopIteration + 1
	
print(printResult)
	
