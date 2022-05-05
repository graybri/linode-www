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
# Name    : if4.py
#
# Purpose :	Demonstrate using int() to convert datatype 
#           to int and assign to a new variable intguess
#           Demonstrate the use of nested if: else: 
#
# Usage   :	./if4.py 
#
#######################################################

# Assign the int value 42 to magic
magic=42

# Prompt and accept keyboard input, assign as str to guess 
guess = input("Guess the magic number: ")

# Convert guess to int datatype and assign to intguess
intguess =int(guess)

# Open parent if: block and test the condition of 2 int values
# being equal
if magic == intguess:
  print(guess + " is correct!!")

# Parent else:
else:
  print("Sorry, " + guess + " is not correct.")

# Calculate the difference of 2 int datatypes
  diff=magic - intguess

# Nested if: else: 
# Note the increased level of indentation
  if diff > -5 and diff < 5:
    print("Close though...")
  else:
    print("Not even close.")
