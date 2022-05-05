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
# Name    : bool.py
#
# Purpose :	Demonstrate the assignment of bool values
#           to variables based on the results of conditional
#           operators
#           Bool values include True and False (no quotes)
#           Bool values can be used in place of conditions 
#           wherever you might use a condition
#           Demonstrate the use of str() function to 
#           convert a bool datatype to a str datatype 
#
# Usage   :	./bool.py 
#
#######################################################

# Evaluate the condition of 5 equaling 5 and assign the
# bool result of True (no quotes) to the variable var1
var1 = 5==5

# Print the bool value of var1
print(var1)

# Evaluate the condition of 5 greater than 25 and assign
# the bool result of False (no quotes) to the variable var2
var2 = 5>25

# if block using the bool value of var2 instead of a condition
# var2 holds False so if block skipped and else block 
# executed
if var2:
# Both sides of the + operator must be the same datatype
# Use the str() function to convert bool value False
# to the str value 'False'
	print("var2 is " + str(var2))
else:
# Both sides of the + operator must be the same datatype
# Use the str() function to convert bool value False
# to the str value 'False'
	print("var2 is " + str(var2))


