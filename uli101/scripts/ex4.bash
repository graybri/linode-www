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
# Name    : ex4.bash
#
# Purpose :	Demonstrate redirecting STDOUT and STDERR
#           for individual commands within the script
#
# Usage   : No options	 
#
#######################################################

# Clear screen
clear

# run a command that produces an error 
echo "To redirect STDOUT and STDERR we can use 1> and 2>"
echo 
echo "attempting to chown a file to root using: chown root ~/Accept*"
echo "note the error"
chown root ~/Accept*
read

# run the command again redirecting STDERR
echo "Sending STDERR to a file called script.err"
echo
chown root ~/Accept* 2> ~/script.err
read

# echo text to STDOUT
echo "Sending STDOUT to a file called script.out"
read

# redirect STDOUT to a file
# Note: after first redirection using >, use >> to append to file
# number 1 optional, echo by itself sends just newline for blank line 
echo "This is the output of ex4.bash" 1> ~/script.out
echo "blah blah blah" 1>> ~/script.out
echo 1>> ~/script.out
echo "Sending STDOUT back to the screen" 1>> ~/script.out
echo
read

echo "Back again"

 

