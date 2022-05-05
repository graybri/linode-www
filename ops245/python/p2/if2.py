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
# Name    : if2.py
#
# Purpose :	Demonstrate the addition of an else: block
#           instead of mutually exclusive if conditions
#
# Usage   :	./if2.py 
#
#######################################################

# Assign str '42' to magic
# Accept keyboard input and assign str to guess
magic='42'
guess = input("Guess the magic number: ")

# Test condition of strings in magic and guess being the same
if magic == guess:
	print(guess + " is correct!!")

# Add else block to print incorrect message is all previous
# conditions evaluate to False
# Note the : and indentation of the else block

else:
	print("Sorry, " + guess + " is not correct.")
