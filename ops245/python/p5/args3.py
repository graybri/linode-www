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
# Name    : args3.py
#
# Purpose :	Demonstrate the addition of an option with
#           a default value and list of available values 
#           Demonstrate if-elif-elif
#
# Usage   :	./args3.py
#           ./args3.py -h
#           ./args3.py 3 4
#           ./args3.py -o divide 3 4
#           ./args3.py -o add 3 4
#           ./args3.py -o subtract 3 4
#           ./args3.py -o multiply 3 4
#
#######################################################

# Import argparse module
import argparse

# Instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

# Add positional arguments (required postional arguments)
parser.add_argument('num1', help='Enter the 1st number', type=int)
parser.add_argument('num2', help='Enter the 2nd numbert', type=int)

# Add options (prefixed with - for short options and -- for long options)
# Include a default value and list of 3 value choices
parser.add_argument('-o', '--operator', help="option for operator",\
		default="add",choices=["add","subtract","multiply"], type=str)

# Parse the command line and assign arguments to args
args = parser.parse_args()

# Test value of operator option and calculate result
if args.operator == "add":
  result=args.num1+args.num2
  print(str(args.num1)+ " plus "+str(args.num2)+" equals: "+str(result))
elif args.operator == "subtract":
  result=args.num1-args.num2
  print(str(args.num1)+ " minus "+str(args.num2)+" equals: "+str(result))
elif args.operator == "multiply":
  result=args.num1*args.num2
  print(str(args.num1)+ " multipied by "+str(args.num2)+" equals: "+str(result))

