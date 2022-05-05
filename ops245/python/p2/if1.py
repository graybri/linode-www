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
# Date    : 2022-05-03
# 
# Name    : if1.py
#
# Purpose :	Demonstrate basic if <condition> block
#           Demonstrate use of mandatory indentation to
#           define start and end of code blocks
#           Demonstrate use of == conditional operator
#           Both values in the condition must be of the 
#           same datatype
#           Other operators !=,<,<=,>,>=
#
# Usage   :	./if1.py
#
#######################################################

# Assign magic number to variable magic
# Note the quotes will assign as a str datatype
magic='42'

# Prompt and accept keyboard input for the guess
# Assign the input to the variable guess
# input() reads the value as str datatype
guess =  input("Guess the magic number: ")

# Test the condition of the 2 str variables being the same
# If condition is True enter the if block defined by 
# indentation.
# If condition is False skip the if block
# Note the : at the end of the if
if magic == guess:
  print(guess + " is correct!!")
  print("Well Done!!")

