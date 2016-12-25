#!/usr/bin/python3

import subprocess

def GetInfo(address, port):
	allresults = []
	callresult = subprocess.check_output(["netcat", address, port])
	callresult = callresult.decode("utf-8")  # convert byte array to string
	disks = callresult.split("||")
	
	for disk in disks:
		diskparts = disk.split("|")
		diskparts.remove("")
		
		drivePath = diskparts[0]
		driveName = diskparts[1]
		temperatureValue = diskparts[2]
		temperatureScale = diskparts[3]
		
		if temperatureScale == "C":
			temperatureValue = (float(temperatureValue) * (9/5)) + 32
			temperatureScale = "F"
		
		formattedInfo = drivePath + " is " + str(temperatureValue) + " " + temperatureScale
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
	
