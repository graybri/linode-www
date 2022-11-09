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
# Name    : file4.py
#
# Purpose : Demonstrate the use of readline() method
#           Demonstrate the looping through the lines 
#           in the file
#           Demonstrate range() function
#
# Usage   : ./file4.py
#           (requires the file test.txt for demonstration)
#
#######################################################

# Not necessary to read in entire contents of file at once
# We can read a single line at a time using the readline( ) method

# Open file in with: block
with open('test.txt','r') as fo:
    # Loop through range of values and print a line
    # Note: the last value of the range ends the loop
    for x in range(1,5):
        # Read the next line of the file with fo.readline() 
        # which returns a single line
        # Strip the new line character
        fo_contents=fo.readline().strip()
        print('Line ' + str(x) + ': ' + fo_contents)




