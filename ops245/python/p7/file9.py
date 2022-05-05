#!/usr/bin/env python3

# Test script to edit a config file
# Reads file contents 
# Loops through lines looking for config settings 
# rebuilds lines 
# writes back to file

infile="test.conf"
outfile="newtest.conf"
newlines=[]
with open(infile,'r') as file1:
	lines=file1.readlines()

for line in lines:
	name,value=line.split('=')
	if name=='NAME':
		value='"newens"'
		line=name+"="+value+"\n"
	newlines.append(line)

with open(outfile,'w') as file2:
	for line in newlines:
		file2.write(line)


