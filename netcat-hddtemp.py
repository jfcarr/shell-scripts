#!/usr/bin/python3

import subprocess

def GetInfo(address, port, desiredScale = "C"):
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

		if driveInfo["Scale"] == "C" and desiredScale == "F":
			driveInfo["Value"] = (float(driveInfo["Value"]) * (9/5)) + 32
			driveInfo["Scale"] = "F"
		
		formattedInfo = driveInfo["Path"] + " is " + str(driveInfo["Value"]) + " " + driveInfo["Scale"]
		allresults.append(formattedInfo)
		
	return allresults

if __name__ == '__main__':
	try:
		allresults = GetInfo("localhost", "7634", "F")
		
		loopIteration = 0
		printResult = ""
		for tempResult in allresults:
			if loopIteration > 0:
				printResult = printResult + ", "
			printResult = printResult + tempResult
			loopIteration = loopIteration + 1
		
		print(printResult)
	
	except Exception as ex:
		print ("[netcat-hddtemp ERROR] " + str(ex))
