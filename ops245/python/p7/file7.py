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
#
# Date    : 2022-11-13
# 
# Name    : file7.py
#
# Purpose : Demonstrate the write() method to write data
#           to the file
#           Demonstrate "write" mode to overwrite the file
#           Demonstrate "append" mode to append to the file
#
# Usage   : ./file7.py
#           (requires test.txt for demonstration)
#           (test.txt can be restored from test.bak)
#
#######################################################

# Loop through file handle one line at a time and print
# old contents
with open('test.txt','r') as fo:
	print("**old contents**")
	for line in fo:
		print(line.strip())
	print()

# Open the file in "write" mode
# write mode will place the file pointer at the
# beginning of the file
# Use the write() method to write 
# (overwriting existing contents) 
with open('test.txt','w') as fo:
  fo.write("new line of text\n")
  fo.write("another new line\n")

# Open file in "read" mode and print new contents
with open('test.txt','r') as fo:
	print("new contents")
	for line in fo:
		print(line.strip())
	print()

# Open file in "append" mode 
# append mode will allow you to add data to the end
# of the existing file (file pointer at the end of the file)
with open('test.txt','a') as fo:
  fo.write("add new line to the end\n")
  fo.write("add another new line to the line\n")

# Open file in "read" mode and print new contents
with open('test.txt','r') as fo:
	print("newest contents")
	for line in fo:
		print(line.strip())
	print()

