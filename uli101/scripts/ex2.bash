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
# Date    : 2022-03-02
# 
# Name    : ex2.bash
#
# Purpose :	Demonstrate and use positional parameters
#           to use command line arguments
#           Demonstrate shifting positional parameters
#
# Usage   : ./ex2.bash one two three four five six	 
#
#######################################################

# Clear screen
clear

# echo contents of $0 - $3
echo "\$0 is: $0"
echo "\$1 is: $1"
echo "\$2 is: $2"
echo "\$3 is: ${3}"
echo

# echo contents of $*, $@  and $#
echo "\$* is a list of all positional values (not including \$0): $*"
echo "\$@ is a list of all positional values (not including \$0): $@"
echo "\$# is the number of positional values (not including \$0): $#"
echo
read

# demonstrate shift command
echo "the shift command can be used to move positional values to the left"
echo "shifting 1:"
shift
echo
echo "this is what the positional values are now: $*"
echo "\$1 is now: $1"
echo 
read

echo "shifting 2"
shift 2
echo
echo "this is what the positional values are now: $*"
echo "\$1 is now: $1"
echo

