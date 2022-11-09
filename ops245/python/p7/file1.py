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
# Date    : 2022-08-17
# 
# Name    : file1.py
#
# Purpose : Demonstrate opwning and reading from a text
#           file.
#           Demonstrate open() function
#           Demonstrate read() method
#           Demonstrate close() method
#
# Usage   : ./file1.py 
#           (Requires file test.txt to be present)	 
#
#######################################################

# Open file and create file object (variable) fo
# Modes include r,a,w,r+,a+
fo=open('test.txt','r')

# Print attributes of fo object (filename and mode)
# Print fo object type
print(fo.name)
print(fo.mode)
print(type(fo))

# Read in contents of file into contents variable
contents=fo.read()

# Strip whitespace using strip() method
print(contents.strip())

# Print object type of contents
print(type(contents))

# Very important to close the file
fo.close()
