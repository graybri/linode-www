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
# Date    : 2022-05-11
# 
# Name    : strings2.py
#
# Purpose :	Demonstrate looping through a string value
#           Demonstrate the upper() string method
#           Demonstrate the lower() string method
#
# Usage   :	./strings2.py 
#
#######################################################

# As well as being able to loop through the characters 
# in a string, there are also methods that can be used on 
# string values.
# We will examine upper() and lower() methods

# Assign and print a string in variable string1
string1='This is a string'
print(string1)
print()

# Loop through the string and print one character at 
# a time in UPPER CASE
# Build string2 an upper case character at a time

# Initialize string2 as an empty string
string2=''

# Loop through string1 a character at a time and 
# print in uppercase using upper() method
# Add each uppercase letter to string2
for character in string1:
	print(': ' + character.upper())
	string2 = string2 + character.upper()

print()

# Print string2
print(string2)
print()

# We can also use lower() method to convert a 
# string to lower case
print(string2.lower())

