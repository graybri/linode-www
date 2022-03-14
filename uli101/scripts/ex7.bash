#!/bin/bash

#
#  ____   ____   	Brian Gray
# | __ ) / ___| 	School of Information Technology
# |  _ \| |  _   	Administration & Security
# | |_) | |_| |_ 	Seneca College
# |____(_)____(_)	brian.gray@senecacollege.ca
#                

########################################################
# Author  : Brian Gray
# Date    : 2022-03-03
# 
# Name    : ex7.bash
#
# Purpose :	Demonstrate for loops
#           Demonstrate looping through positional 
#           parameters
#           Demonstrate looping through file contents
#           Demonstrate command substitution
#
# Usage   :	./ex7.bash list of items for shopping list
#
#######################################################

# Clear screen
clear

# for loops loop through a list of values
# lists can be hard coded, supplied through a variable,
# or provided using a technique called command substitution
# $* contains the list of positional parameters (command arguments)
# take one value at a time from list and assign to variable item
# echo the item and append to the file shopping list
for item in $*
do
	echo "$item" >> shopping.list
done

# use for loop to loop through contents of shopping.list file
# one line at a time using command substitution $(command)
# take one value at a time from list and assign to variable item
# echo the item to the screen
echo "Don't forget to pick up:"
for item in $(cat shopping.list)
do
	echo $item
done
echo 

# use for loop to loop through hard coded list of values
for x in 5 4 3 2 1 "Go Shopping!!"
do
	echo $x
	sleep 1
done


