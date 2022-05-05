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
# Name    : if3.py
#
# Purpose :	Demonstrate the addition of a nested if block
#           Demonstrate the use of int() to convert a 
#           str to an int
#           Demonstrate the calculation of diff (int)
#           Demonstrate the use of multiple conditions 
#           separated by 'and' keyword 
#
# Usage   :	./if3.py 
#
#######################################################

# Assign magic number to variable magic
# Note the missing quotes around 42 which means it will
# be assigned int datatype
magic=42

# Prompt and accept keyboard input for the guess
# input() reads the value as a str datatype
guess = input("Guess the magic number: ")

# Test the condition of maic and guess being the same
# Note the use of the int() function to convert the 
# datatype of guess so that the datatypes match
if magic == int(guess):
  print(guess + " is correct!!")
else:
  print("Sorry, " + guess + " is not correct.")

# Calculate the difference betwen the magic numbe and guess
# Note the use of the int() function again to convert the
# datatype of guess  
  diff=magic - int(guess)

# Add nested if block, note the extra level of indentation 
# which indicates that it is included as part of the parent
# else: block 

# The if condition is testing 2 separate conditions separated
# by the 'and' keyword that means both conditions must evaluate
# to True for the if block to be executed 
  if diff > -5 and diff < 5:
    print("Close though...")
