#!/usr/bin/env python3

#Create a list called names
names=['brian','lisa','steve','mary']

#Print the list
print(names)
print()

#Print individual values from the list using the [index]
print("The first name is: " + names[0])
print("The third name is: " + names[2])
print()

#Printing all of the list values using a for loop 
for nam in names:
	print(nam)
print()

#Adding a value to the end of a list
names.append('jack')

#Inserting a value into the third position in the list
names.insert(2,'suzie')

#Printing all of the list values using a for loop 
for nam in names:
	print(nam)
print()

#Creating a 2nd list
newnames=['mario','jennifer']

#Extend a list by appending another list
names.extend(newnames)

#Printing all of the list values using a for loop 
for nam in names:
	print(nam)
print()

