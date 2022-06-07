#!/usr/bin/env python3

#
#  ____   ____   	Brian Gray
# | __ ) / ___| 	School of Information Technology
# |  _ \| |  _   	Administration & Security
# | |_) | |_| |_ 	Seneca College
# |____(_)____(_)	brian.gray@senecacollege.ca
#                
########################################################
# Author  : Brian Gray
# Date    : 2022-06-06
# 
# Name    : args2.py
#
# Purpose :	Demonstrate the addition of an option to
#           the parser object, that allows a file argument
#
# Usage   :	./args2.py -h, ./args2.py, ./args2.py 1st 2nd,
#            ./args2.py -f test.txt 1st 2nd
#
#######################################################

# Import arparse module
import argparse

# Instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

# Add positional arguments (required postional arguments)
parser.add_argument('arg1', help='Enter the first argument', type=str)
parser.add_argument('arg2', help='Enter the 2nd argument', type=str)

# Add options (prefixed with - for short options and -- for long options)
parser.add_argument('-f', '--file', help="option for filename", type=str)

# Parse the command line and assign arguments to args
args = parser.parse_args()

# Print out the 2 required arguments
print("The first argument was: "+args.arg1)
print("The second argument was: "+args.arg2)

# If -f/--file option supplied, print filename
if args.file != None:
  print("The optional filename is: "+str(args.file))




