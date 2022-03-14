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
# Name    : ex6.bash
#
# Purpose :	Demonstrate set for positional parameters
#           Demonstrate if-elif-else-fi control structure
#           Demonstrate test [  ] command
#           Numerical comparison operators
#           Text comparison operators
#           File tests
#
# Usage   :	No options
#
#######################################################

# Clear screen
clear

# Use set command to set positional parameter values
set 58 745 ~/file1 Sean Shawn

# if structures are used to execute commands based on the
# test of a condition.
# tests result in a value of True (0) or False (1 or non-zero)

# use test [] command to compare two mumeric values 
# using -gt operator
if [ $2 -gt $1 ]
then
	echo "$2 is greater than $1"
# test 2nd condition using elif	
elif [ $1 -gt $2 ]
then
	echo "$1 is greater than $2"
# else captures all other conditions
else
	echo "$1 and $2 are equal"
fi
echo
read

# if structure to test [] file condition
# ! is used to invert test
# man test to view condition tests available
# elif and else not required
if test ! -f $3 
then
	echo "The file $3 is not present"
fi
echo
read

# if structure to test string comparison
# ! is used to invert test
if [ ! $4 = $5 ]
then
	echo "$4 and $5 are not the same"
else 
	echo "$4 and $5 are the same"
fi


