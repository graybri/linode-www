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
# Name    : twoif.py
#
# Purpose :	Demonstrate the use of two if blocks to
#           Mutually exclusive conditions
#           Demonstrate the use of int() to convert a 
#           str to an int datatype
#
# Usage   :	./twoif.py
#
#######################################################

# Assign int value 42 to variable magic
magic=42

# Accept keyboad input and assign to variable guess as 
# str datatype
guess = input("Guess the magic number: ")

# Convert guess to int and assign to intguess
intguess = int(guess)

# Create 2 if blocks to handle 2 different conditions
# that have mutually exclusive results (both can't be True)
# Note the level of indentation is the same, so not nested. 
if magic == intguess:
	print(guess + " is correct!!")
if magic != intguess:
	print("Sorry, " + guess + " is not correct.")
