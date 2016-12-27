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
		
		# Sample input: |/dev/sda|WDC WD20EARX-00PASB0|34|C||/dev/sdb|WDC WD10EZEX-00BN5A0|33|C|
		callresult = subprocess.check_output(["netcat", self.address, str(self.port)])
		callresult = callresult.decode("utf-8")  # convert byte array to string
		disks = callresult.split("||")  # split into one disk per line
		
		for disk in disks:  
			diskparts = disk.split("|")  # parse out the individual info for each disk
			diskparts.remove("")  # remove any leading and/or trailing empty entries
			
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
		
		# Sample output: /dev/sda is 95.0 F, /dev/sdb is 91.4 F
		if allresults:
			print(str.join(", ", allresults))
		
if __name__ == '__main__':
	try:
		myHDDTemp = HDDTemp("localhost", 7634, "F")
		myHDDTemp.ShowInfo()
	
	except Exception as ex:
		print ("[netcat-hddtemp ERROR] " + str(ex))
