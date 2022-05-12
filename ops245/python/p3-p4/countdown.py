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
# Name    : countdown.py
#
# Purpose :	Demonstrate create a list
#           For loop through the list to print a countdown
#           Add else: block to for loop to execute after 
#           loop iterations are complete.
#
# Usage   :	./countdown.py 
#
#######################################################

# This script will show that we can add an else: block
# to a for loop.
# The else: block will execute after the final iteration
# of the loop

# Import required modules
import os

# Create list of strings from '10' to '1'
countdown=['10','9','8','7','6','5','4','3','2','1']

# for loop to loop throught the list
# else: block will execute after the last iteration of
# the loop
# Note the use of indentation to define blocks
# Note the use of the :
for count in countdown:
	print("--> " + count)
	os.system('sleep 1')
else:
	print("Blast Off!!")


