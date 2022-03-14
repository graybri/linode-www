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
# Date    : 2022-03-04
# 
# Name    : ex10.bash
#
# Purpose :	Demonstrate while loops which loop as long
#           as a condition evaluates to True (0) 
#           Uses a while loop to prompt user for items to 
#           add to the shopping.list file until they 
#           type 'quit'
#           Uses 2nd and 3rd while loop to read lines from
#           the shopping.list file one a time, while read
#           is successful echo the line
#
# Usage   :	 No options
#
#######################################################

# Clear screen
clear 

# Empty contents of shopping.list
cat "/dev/null" > shopping.list

# Use a while loop to accept shopping items. 
# loop while $input does not equal 'quit'
# User types quit to end loop/list
while [ "$input" != "quit" ]
do
	echo -n "Enter an item:"
	read input
	
	# dont add quit to shopping list
	if [ "$input" != "quit" ]
	then
		echo $input >> shopping.list
	fi
done

echo "Thanks for adding items"
echo
echo "Your complete shopping list is:"

# Example #1
# Supply contents of shopping list to while loop through a pipe from cat
# loop executes while the read command is successful. 
# read returns status code 0 (True) as long as there is a line to read
# read returns status code 1 (False) when the end of the file is reached
cat shopping.list |
while read input
do
	echo $input
done
read

echo
echo "Your complete shopping list is:"
# Example #2
# Supply contents of shopping list to while loop through STDIN redirection
# loop executes while the read command is successful. 
# read returns status code 0 (True) as long as there is a line to read
# read returns status code 1 (False) when the end of the file is reached
while read input
do
	echo $input
done < shopping.list
