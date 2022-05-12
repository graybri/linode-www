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
# Name    : countdown3.py
#
# Purpose :	Demonstrate that the else: block will
#           executes even if the while condition never
#           evaluates to True
#
# Usage   :	./countdown3.py 
#
#######################################################

# This script will demonstrate a while loop that includes an else: block.
i# The else: block will execute even if the condition never evaluates to true

# Import required modules
import os

#Set count to a negative int value
count=-10

# The while loop condition will evaluate to False
# The else: block will execute anyway
while count > 0:
	print("--> " + str(count))
	os.system('sleep 1')
	count=count-1
else:
	print("Blast Off!!")


