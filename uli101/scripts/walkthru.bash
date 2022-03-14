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
# Name    : walkthru.bash
#
# Purpose :	Example script used to demonstrate a script 
#           walkthru
#           3 different command lines demonstrated 
#
# Usage   :	./walkthru.bash
#           ./walkthru.bash L0m1j0 CAtsDogs M3H2t7 2P5c5Y
#           ./walkthru.bash m3T1d6 PostaL l2M4t5 
#
#######################################################

# Clear screen
clear

validcount=0
invalidcount=0

if [ $# -eq 0 ]
then
	echo "Please enter at least one valid postal code"
	exit 1
fi

for item in $*
do
	echo $item | grep -i "^[a-z][0-9][a-z][0-9][a-z][0-9]$" > /dev/null
	if [ $? = 0 ]
	then
		validcount=$(( $validcount+1 ))
		item=$(echo $item| tr 'a-z' 'A-Z')
		echo "$item is valid"
	else
		invalidcount=$(( $invalidcount+1 ))
		item=$(echo $item| tr 'A-Z' 'a-z')
		echo "$item is invalid"
	fi
done

if [ $invalidcount -ge 2 ]
then
	echo "Too many invalid Postal Codes"
	echo "Quiting"
	exit 2
fi

