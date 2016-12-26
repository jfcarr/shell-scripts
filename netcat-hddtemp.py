#!/usr/bin/python3

import subprocess

class HDDTemp:
	def __init__(self, address, port, desiredScale = "C"):
		self.address = address
		self.port = port
		self.desiredScale = desiredScale
		
	def GetInfo(self):
		allresults = []
		driveInfo = {"Path": "", "Name": "", "Value": 0, "Scale": "C"}
		callresult = subprocess.check_output(["netcat", self.address, str(self.port)])
		callresult = callresult.decode("utf-8")  # convert byte array to string
		disks = callresult.split("||")
		
		for disk in disks:
			diskparts = disk.split("|")
			diskparts.remove("")
			
			driveInfo["Path"] = diskparts[0]
			driveInfo["Name"] = diskparts[1]
			driveInfo["Value"] = diskparts[2]
			driveInfo["Scale"] = diskparts[3]
	
			if driveInfo["Scale"] == "C" and self.desiredScale == "F":
				driveInfo["Value"] = round((float(driveInfo["Value"]) * (9/5)) + 32, 1)
				driveInfo["Scale"] = "F"
			
			formattedInfo = driveInfo["Path"] + " is " + str(driveInfo["Value"]) + " " + driveInfo["Scale"]
			allresults.append(formattedInfo)
			
		return allresults
	
	def ShowInfo(self):
		allresults = self.GetInfo()

		loopIteration = 0
		printResult = ""
		for tempResult in allresults:
			if loopIteration > 0:
				printResult = printResult + ", "
			printResult = printResult + tempResult
			loopIteration = loopIteration + 1
		
		print(printResult)

if __name__ == '__main__':
	try:
		myHDDTemp = HDDTemp("localhost", 7634, "F")
		myHDDTemp.ShowInfo()
	
	except Exception as ex:
		print ("[netcat-hddtemp ERROR] " + str(ex))
