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
# Date    : 2022-04-27
# 
# Name    : first.py
#
# Purpose :	Demonstrate print() function
#           Demonstrate assigning int str float bool
#           datatype to variables
#           Demostrate type() function
#           Demonstrate input() function
#           Demonstrate +-\* operators
#
# Usage   :	./first.py
#
#######################################################

# Print a string in quotes
print ("This is a test")

# Print a blank line
print()

# Assign int str float and bool to a variable
# Variable names must start with a letter or _
# int - Whole Numbers
# str - Strings of text bounded by quotes
# float - Decimal values
# boolean - True or False (No quotes)
num1 = 3
str1 = "this is a string"
num2 = 3.14
boo1 = True
boo2 = False

# Print variables with print() function
print(num1)
print(str1)
print(num2)
print(boo1)
print(boo2)

# Print the output of the type() function
# type() returns the datatype of a variable
print(type(num1))
print(type(str1))
print(type(num2))
print(type(boo1))

# Use the input() function to read a line from STDIN
# input() reads the line as str
# Assign result of input to variable, str datatype
data1=input("Please enter your section: ")

# Use the + operator to join strings and variables that
# contain strings
# When using an operator the datatypes of the operands
# must match
print("Your section is " + data1)
print()

# Assign 2 variables with int values
# Print the sum of the two variables using the + operator
# Print the product of the two variables using the * operator
# The datatypes of the operands must match
x=200
y=4
print(x+y)
print(x*y)

