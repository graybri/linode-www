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
# Name    : 
#
# Purpose :	 
# 
#
#
# Usage   :	 
#
#######################################################




import argparse


#instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

#Add positional arguments (required postional arguments)
parser.add_argument('arg1', help='Enter the first argument', type=str)
parser.add_argument('arg2', help='Enter the 2nd argument', type=str)

#Add options (prefixed with - for short options and -- for long options)
parser.add_argument('-f', '--file', help="option for filename", type=str)

#Parse the command line and assign arguments to args
args = parser.parse_args()

print("The first argument was: "+args.arg1)
print("The second argument was: "+args.arg2)
if args.file != None:
  print("The optional filename is: "+str(args.file))




