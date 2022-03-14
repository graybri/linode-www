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
# Name    : ex5.bash
#
# Purpose :	Demonstrate redirection within a script to
#           override redirection from the command line
#           Demonstrate addition of custom error 
#           messages to error log
#
# Usage   :	./ex5.bash 2> script.err 
#
#######################################################

# Clear screen
clear

# run a command that produces an error
# script executed with 2> script.err 
# error won't be displayed
echo "This is output"
echo "This command generates an error"
chown root ~/Accept*
echo
read

# Create a custom error message by echoing to STDOUT
# But redirect to STDERR file location 
echo "This is a custom error message" 1>&2
echo
read

# Override STDERR to send to display
echo "This command generates an error that is redirected to STDOUT"
chown root ~/Accept* 2>&1



