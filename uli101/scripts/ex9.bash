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
# Name    : ex9.bash
#
# Purpose :	Demonstrate bash integer arithmetic 
#           Demonstrate script requirement tests
#           Demonstrate arithmetic substitution
#
# Usage   :	./ex9.bash 2 5 8 11 
#
#######################################################

# Clear screen
clear

# Sanity checks
# Test the conditions for successful script execution
# before proceeding
# exit with non-zero status code if conditions not met
# check for 4 command arguments
if [ $# != 4 ]
then
	echo "This script requires 4 integer arguments."
	exit 1
fi

# Solve expression and assign result to variable x
(( x=$1+$2 ))
# Output results
echo "$1 plus $2 = $x "
echo

# Solve expressions and output result using arithmetic substitution
# expressions solved outside of " "
echo "$3 minus $4 = " $(($3-$4))
echo "$1 multiplied by $3 = " $(( $1 * $3 ))
echo

# Solve expression, substitute result, assign to variable
x=$(( $1 + $2 + $3 + $4 ))
echo "All 4 arguments added together = $x"
