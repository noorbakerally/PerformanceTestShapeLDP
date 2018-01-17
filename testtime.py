import numpy
from rdflib import Graph
import json
import os
import subprocess
import urllib
import copy
import os

jarPath = "/home/noor/Documents/repositories/github/ShapeLDP/target/ShapeLDP-1.0-SNAPSHOT.jar"
designDocumnent = "d2.ttl"
sources = os.listdir("datasets")
obj = {"name":"","times":[],"RM":0,"mean":0,"median":0,"sd":0}
objs = {}
j = 1
for nameInt in range(50,27050,50):
	name = str(nameInt) 
	print "##############"+str(j)
	j = j + 1
	catalog = copy.deepcopy(obj)
	catalog["name"] = name
	i = 0
	for i in range(5):
		command = "java -jar "+jarPath+" -d "+designDocument+" -o 0 -if datasets/" + name 
		print command 
		output = subprocess.check_output(command, shell=True)
		start = output.index("#start")+7
		end = output.index("#end")-1
		output = output[start:end].split(",")
		exeTime = output[0]
		rm = output[1]
		
		catalog["times"].append(long(exeTime))
		catalog["RM"] = long(rm)
	
	catalog["mean"] = round(numpy.mean(catalog["times"]))
	catalog["median"] = numpy.median(catalog["times"])	
	catalog["sd"] = numpy.std(catalog["times"])	

	#set number of triples
        catalog["numtriples"] = int(name) + 6

	objs[name] = catalog	
	with open("results/"+name, 'w+') as outfile:
    		json.dump(catalog, outfile)
	os.system("echo '"+name+"' > counter")
