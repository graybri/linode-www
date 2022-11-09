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
# Date    : 2022-08-19
# 
# Name    : file5.py
#
# Purpose : Demonstrate looping directly through file object
#
# Usage   : ./file5.py
#           (requires test.txt for demonstration)
#
#######################################################

# We can also directly loop through the lines of the 
# file by looping on the file object

# Open file in with: block
with open('test.txt','r') as fo:
    # Loop through the lines one at a time and print
    # Reads a line from fo into string 'line'
    for line in fo:
        line=line.strip()
        print("The line is: " + line)

