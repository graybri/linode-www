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
# Date    : 2022-08-10
# 
# Name    : notry.py
#
# Purpose : Demonstrate a file operation of opening a 
#           file that can raise various exceptions, 
#           Without handling exceptions
#           Run opening a readonly file (test.ro)
#           Run opening a file that does not exist (test.rw)
#
# Usage   : ./notry.py	 
#
#######################################################

# Demo opening of files without using try: except: finally:

# Prompt for filename (test.ro)
file=input('Enter a filename: ')

# Open file for read/write creating a filehandle object (fo)
fo=open(file, "r+")

# Read in contents of the file
content=fo.read()

# Output contents
print('Contents : ' + content)

# Close file
fo.close()

print('thanks')

