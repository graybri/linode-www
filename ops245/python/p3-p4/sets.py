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
# Name    : sets.py
#
# Purpose :	Demonstrate the creation and use of a set
#           Demonstrate the printing of a set
#           Demonstrate looping throught the contents
#           of a set
#           Demonstrate adding values to a set using the
#           add() method
#
# Usage   :	./sets.py 
#
#######################################################

# Sets are similar to lists, they contain a list of 
# values
# We use {} instead of [] to define a set
# Values in a set are accessed in random order
# There are no index numbers
# Sets cannot contain duplicate values

# Create a set called cities (notice the {})
cities={'Ottawa','London','Paris','Beijing'}

# Print the set (not ordered)
print(cities)
print()

# Printing all of the set values using a for loop 
for city in cities:
	print(city)

print()

# We can add values to a set using the add() method
cities.add('Rome')
cities.add('Delhi')

# Printing all of the set values using a for loop 
for city in cities:
	print(city)

print()
