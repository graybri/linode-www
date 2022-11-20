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
# Name    : ex8.bash
#
# Purpose :	Demonstrate the use of exit status codes 
#           contained in the variable $?
#           Demonstrate exiting the script with custom
#           exit status codes representing different 
#           error conditions
#
# Usage   :	No options 
#
#######################################################

# Clear screen
clear

# Create an empty file in home directory
# Check value of $? for success message
cd $HOME
echo "creating file $HOME/ex8.sample"
touch ex8.sample
if [ $? ] 
then
	echo "Command Successful"
else
	echo "Command Unsuccessful"
fi
echo
read

# Alternate method
# Check value of $? for success message
echo "creating file $HOME/ex8.sample"
if touch ex8.sample
then
	echo "Command Successful"
else
	echo "Command Unsuccessful"
fi
echo
read

# Remove the file
# echo value of $? 
echo "removing ex8.sample"
rm ex8.sample
echo "Exit Status: $?"
echo
read

# Attempt to remove te file a 2nd time
# command will fail
# $? will be 1
echo "removing ex8.sample again"
rm ex8.sample
echo "Exit Status: $?"
echo
read

# Test for existence of file to exit script with custom exit status
# script will exit with status code 2
if [ ! -f ex8.sample ]
then
	echo "exiting with status 2"
	exit 2
else 
	echo "exiting with status 6"
	exit 6
fi


