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
# Name    : ex3.bash
#
# Purpose :	Demonstrate the use of 'set' to override 
#           positional parameter values inline 
#
# Usage   :	./ex3.bash I hate winter
#
#######################################################

# Clear screen
clear

# echo positional parameter valuse from command arguments
echo "The positional parameters are: $*"

# save original values ino new variables
echo "Saving original parameters to user defined variables"
arg1=$1
arg2=$2
arg3=$3
echo
read

# use set to override command arguments
echo "Using set to assign new values"
set bring on summer
echo
echo "the new positional parameters are: $*"
echo
echo "luckily I saved my original values first: ${arg1} ${arg2} ${arg3}"
echo

