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
# Name    : args4.py
#
# Purpose :	Demonstrate the addition of 3 options 
#           that don't require a value but will value
#           True if the option is used, False if not
#           
# Usage   :	./args4.py
#           ./args4.py -h
#           ./args4.py 3 4
#           ./args4.py -a 3 4  
#           ./args4.py -s 3 4  
#           ./args4.py -a -s -m 3 4  
#
#######################################################

# Import argparse module
import argparse

# Instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

# Add positional arguments (required postional arguments)
parser.add_argument('num1', help='Enter the 1st number', type=int)
parser.add_argument('num2', help='Enter the 2nd number', type=int)

# Add 3 options (prefixed with - for short options and -- for long options)
# If option is used it will be set to boolean True
parser.add_argument('-a', '--add', help="option for addition", action="store_true")
parser.add_argument('-s', '--subtract', help="option for subtraction", action="store_true")
parser.add_argument('-m', '--multiply', help="option for multiplication", action="store_true")

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


