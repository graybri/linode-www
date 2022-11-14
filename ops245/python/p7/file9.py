#!/usr/bin/env python3
#
#  ____   ____   	Brian Gray
# | __ ) / ___| 	School of Information Technology
# |  _ \| |  _   	Administration & Security
# | |_) | |_| |_ 	Seneca College
# |____(_)____(_)	brian.gray@senecacollege.ca
#                

########################################################
# Author  : Brian Gray
# Date    : 2022-11-13
# 
# Name    : file9.py
#
# Purpose : Demonstrate the task of editing config files
#           with a python script
# 
# Usage   : ./file9
#           (requires original ifcfg.conf)
#           (will create newifcfg.conf)
#           (ifcfg.conf can be restored from ifcfg.conf.bak)
#
#######################################################

# A common task for system admins is to modify config 
# files
# This script is an example of editing a config file
# It will read the original file contents looping through
# the lines
# It will examine each line looking for config settings 
# If desired it will rebuild the line using a new value 
# Writes the lines to an output file that will contain
# the new lines and then copy the ouput file back to the 
# original filename

# Set input and output filenames
infile="ifcfg.conf"
outfile="newifcfg.conf"

# Initialize lists
lines=[]
newlines=[]

# Open the input file and readlines() into list
with open(infile,'r') as file1:
    lines=file1.readlines()

# Loop through list of lines
# Split lines into to name and value using split() method
# If the name field is "NAME" change the value field
# Add the line to newlines list
for line in lines:
    name,value=line.split('=')
    if name=='NAME':
        value='"newens"'
        line=name+"="+value+"\n"
    newlines.append(line)

# Open output file in "write" mode
# Loop newlines list and write the line to the ouput file
with open(outfile,'w') as file2:
    for line in newlines:
        file2.write(line)

## You can then add the code to copy the file back to the
## original name








