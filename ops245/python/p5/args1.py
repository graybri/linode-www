#!/usr/bin/env python3

'''
  ____   ____   	Brian Gray
 | __ ) / ___| 	    School of Information Technology
 |  _ \| |  _   	Administration & Security
 | |_) | |_| |_ 	Seneca College
 |____(_)____(_)	brian.gray@senecacollege.ca
'''                
########################################################
# Author  : Brian Gray
# Date    : 2022-05-13
# 
# Name    : args1.py
#
# Purpose : Introduce the argparse module used for 
#           accepting command line arguments into 
#           python scripts
#           Demonstrate creation of parser object
#           Demonstrate adding required command arguments
#           Demonstrate parse_args() method to parse 
#           command line
# 
# Usage   :	./args1.py arg1 arg2 & ./args1.py -h 
#           & ./args1.py  
#
#######################################################

# Import the argparse module
import argparse

# Instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

# Print object type of parser
print(type(parser))

# Add 2 required positional arguments
parser.add_argument('arg1', help='Enter the first argument', type=str)
parser.add_argument('arg2', help='Enter the second argument', type=str)

# Create args object (dictionary) using parse_args() method on parser object
args=parser.parse_args()

# Assign arguments to local variables
argument1=args.arg1
argument2=args.arg2

# Print values of arguments
print('Arg1 is: ' + argument1)
print('Arg2 is: ' + argument2)
