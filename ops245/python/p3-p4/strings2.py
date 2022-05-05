#!/usr/bin/env python3

#Assign and print a string
string1='This is a string'
print(string1)
print()

#Loop through the string and print one character at a time in UPPER CASE
#Build string2

string2=''
for character in string1:
	print(': ' + character.upper())
	string2 = string2 + character.upper()
print()

#Print string2
print(string2)
print()

