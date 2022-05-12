#!/usr/bin/env python3

'''
  ____   ____   	Brian Gray
 | __ ) / ___| 	    School of Information Technology
 |  _ \| |  _   	Administration & Security
 | |_) | |_| |_ 	Seneca College
 |____(_)____(_)	brian.gray@senecacollege.ca
'''                
########################################################
# Author  : Brian Gray
# Date    : 2022-05-12
# 
# Name    : countdown2.py
#
# Purpose :	Demonstrate a while loop (conditional) loop
#           Demonstrate str() function
#           Demonstrate adding an else: block to a 
#           while loop
#
# Usage   :	./countdown2.py 
#
#######################################################

# This script will demonstrate a while loop that includes 
# an else: block.
# A while: loop is a conditional loop
# It tests a condition and as long as that condition 
# evaluates to True it will continue to loop
# When the condition evaluates to False it will execute 
# the else: block if available, and stop looping.

# Import required modules
import os

# Initialize int datatype variable count
count=10

# while loop tests the condition that count is greater than 0
# Note the indentation to define the block and the use of :
while count > 0:
# Print count using str()
	print("--> " + str(count))
	os.system('sleep 1')
# Decrease count by 1
	count=count-1
# else: block executes when condition is False
else:
	print("Blast Off!!")


