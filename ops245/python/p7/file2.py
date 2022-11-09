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
# Name    : file2.py
#
# Purpose : Demonstrate the use of a context manager  
#           Demonstrate the use of with: block
#           Demonstrate the automatic close
#
# Usage   : ./file2.py
#           (requires test.txt for demonstration)
#
#######################################################

# Open file and create file object fo
# Modes include r,a,w,r+,a+
# Alternate method no need to close
# Using context manager with: block
# File automatically closes when block ends

print("enter block")

# Start with: block as a context manager
# Create file handle object (variable) 'fo'
with open('test.txt','r') as fo:
    # Print attributes
    print(fo.mode)
    print(fo.name)
    
    # Read contents of file to variable
    fo_contents=fo.read()
    print(fo_contents)
    
    # See file if is not closed (boolean attribute)
    print(fo.closed)

# Exit block
print("exit block")
print(fo.mode)

# See if file is closed
print(fo.closed)




