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
# Date    : 2022-08-18
# 
# Name    : file3.py
#
# Purpose : Demonstrate the readlines() method as
#           opposed to read()
#           Demonstrate looping through returned list of
#           lines
#
# Usage   : ./file3.py
#           (requires test.txt for demonstration)
#
#######################################################

# Not always practical to use fo.read() method
# read() returns entire file contents as a string
# readlines() returns entire contents as a list of lines
# Allows us to easily loop through the list to process lines

# Open file within with: block
with open('test.txt','r') as fo:
    # read contents of file to variable using fo.readlines() which returns
    # a list of lines
    fo_contents=fo.readlines()
    print(fo_contents)

# Loop through list of lines
# Strip off newline character
for line in fo_contents:
    print('>> ' + line.strip())




