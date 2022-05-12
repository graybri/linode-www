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
# Date    : 2022-05-10
# 
# Name    : lists.py
#
# Purpose :	Demonstrate the use of lists
#            - creation
#            - indexes
#            - append() method
#            - insert() method
#            - extend() method
#           Demonstrate use of for loops
#
# Usage   :	./lists.py 
#
#######################################################

# lists are a datatype (object) that hold a list of 
# multiple values that can be referenced by index
# position.
# Similar to arrays in other languages

# The list is created  by assigning a comma separated 
# list of values, enclosed in [] brackets, to a variable 

# Create a list called names
names=['brian','lisa','steve','mary']

# Print the list in its entirety
print(names)
print()

# Print individual values from the list using the [index]
# index values start at 0
print("The first name is: " + names[0])
print("The third name is: " + names[2])
print()

# Printing all of the list values using a for loop
# Takes a value from the list names and assigns to 
# variable nam
# Note the use of indentation to mark the lines in the
# for loop block
# Note the use of ':' in the syntax
for nam in names:
	print(nam)
print()

# Adding a value to the end of a list is done with 
# the append() method
names.append('jack')

# Inserting a value into the list is done with the
# insert() method.
# The insert() accepts 2 arguements, the index position 
# and the new value
# Insert 'suzie' into the third position in the list
names.insert(2,'suzie')

# Printing all of the list values using a for loop 
for nam in names:
	print(nam)
print()

# Creating a 2nd list
newnames=['mario','jennifer']

# Add (append) a list to an existing list using the extend()
# method
names.extend(newnames)

# Printing all of the list values using a for loop 
for nam in names:
	print(nam)
print()

