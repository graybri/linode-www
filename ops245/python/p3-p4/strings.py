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
# Name    : strings.py
#
# Purpose :	Demonstrate looping through characters in
#           a string
#
# Usage   :	./strings.py 
#
#######################################################

# It is also possible to loop through a string value 
# one character at a time

#Assign and print a string
string1='This is a string'
print(string1)
print()

# Loop through the string and print one character at a time
# Note the use of indentation to define the block and :
for character in string1:
	print(': ' + character)

print()


