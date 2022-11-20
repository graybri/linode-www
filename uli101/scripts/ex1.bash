#!/bin/bash
#
#  ____   ____   	Brian Gray
# | __ ) / ___| 	School of Information Technology
# |  _ \| |  _   	Administration & Security
# | |_) | |_| |_ 	Seneca College
# |____(_)____(_)	brian.gray@senecacollege.ca
#                
########################################################
# Author:	 Brian Gray
# Date:		 2022-03-02
# 
# Name    : ex1.bash
#
# Purpose :	Demonstrate echo, echo -n, printf, variables,
#			variable substitution, soft vs hard quotes,
#			read keyboard input
#           Demonstrate using an evvironment vaiable
#
# Usage   : No options	 
#
#######################################################

# Clear screen
clear

# echo vs echo -n
echo "Two"
echo "Lines"
echo -n "One"
echo "Line"
echo
read

# User input

# printf a prompt
printf "enter your first name: "

# read line from keyboard and assign to variable
read fname

# echo a prompt using -n
echo -n "enter your last name: "

# read line from keyboard and assign to variable
read lname

# show a prompt and read from keyboard to a variable
read -p "enter your age: " age

read

# Variable substitution using 2 different syntax
# soft or double quotes vs hard quotes
echo 
echo "Hello, my first name is $fname."
echo "My last name is ${lname}." 
echo 'My age is ${age}'
echo "My age is ${age}"
echo

read

# Assign a value to a variable 
# = is the assignment operator
# No spaces around the operator
course="ULI101"
college="Seneca College"
echo "I am currently enrolled in ${course}, at ${college}."

# Single quotes vs Double quotes
echo 'I am currently enrolled in ${course}, at ${college}.'

read
# Demonstrate using Environment Variables
echo "My login name is $USER"
echo "My home directory is $HOME"
echo "My shell is $SHELL"

