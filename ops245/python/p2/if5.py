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
# Date    : 2022-05-04
# 
# Name    : if5.py
#
# Purpose :	Demonstrate use of elif block used in place of 
#           nested if: else:
# 
# Usage   :	./if5.py 
#
#######################################################

# Prepare and assign all variables
magic=42
guess = input("Guess the magic number: ")
intguess = int(guess)
diff=magic - intguess

# if:... elif:... else: structure
# Removed nested if and replaced with an elif block
# Use one or more elif blocks to test secondary conditions
# if previous if conditions evaluate to false
# Multiple elif blocks can be used to test secondary conditions
# Whichever condition evaluates True first is the block 
# to be executed 
# Note the consistent level of indentation and the use of :
if magic == intguess:
  print(guess + " is correct!!")
elif diff > -5 and diff < 5:
  print("Close though...")
else:
  print("Not even close.")
