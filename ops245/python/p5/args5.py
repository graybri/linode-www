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
# Date    : 2022-06-07
# 
# Name    : args5.py
#
# Purpose : Demonstrate the use of a mutually exclusive
#           group of options
# 
# Usage   : ./args5.py
#           ./args5.py -h
#           ./args5.py 2 6
#           ./args5.py -a 2 6
#           ./args5.py -m 2 6
#           ./args5.py -s 2 6
#           ./args5.py -a -s 2 6
#
#######################################################

# Import argparse module
import argparse

# Instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

# Add positional arguments (required postional arguments)
parser.add_argument('num1', help='Enter the 1st number', type=int)
parser.add_argument('num2', help='Enter the 2nd number', type=int)

# Create a mutually exclusive group of options
group = parser.add_mutually_exclusive_group()

# Add options into the mutually exclusive group set to True if used
group.add_argument('-a', '--add', help="option for addition", action="store_true")
group.add_argument('-s', '--subtract', help="option for subtraction", action="store_true")
group.add_argument('-m', '--multiply', help="option for multiplication", action="store_true")

# Parse the command line and assign arguments to args
args = parser.parse_args()

# Check which option is used by testing for True
# Calculate and print result
if args.add:
  result=args.num1+args.num2
  print(str(args.num1)+ " plus "+str(args.num2)+" equals: "+str(result))
elif args.subtract:
  result=args.num1-args.num2
  print(str(args.num1)+ " minus "+str(args.num2)+" equals: "+str(result))
elif args.multiply:
  result=args.num1*args.num2
  print(str(args.num1)+ " multipied by "+str(args.num2)+" equals: "+str(result))
else:
  print("No operator specified")


