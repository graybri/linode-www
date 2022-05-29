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
#
#
# Usage   :	 
#
#######################################################




import argparse


#instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')
print(type(parser)
#Add positional arguments (required postional arguments)
parser.add_argument('arg1', help='Enter the first argument', type=str)
parser.add_argument('arg2', help='Enter the 2nd argument', type=str)

#Parse the command line and assign arguments to args
args = parser.parse_args()
print(type(args)
#Assign local variables args values
arg1 = args.arg1
arg2 = args.arg2

print("The first argument was: "+arg1)
print("The second argument was: "+arg2)





