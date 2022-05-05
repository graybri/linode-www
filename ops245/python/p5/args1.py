#!/usr/bin/env python3

import argparse


#instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

#Add positional arguments (required postional arguments)
parser.add_argument('arg1', help='Enter the first argument', type=str)
parser.add_argument('arg2', help='Enter the 2nd argument', type=str)

#Parse the command line and assign arguments to args
args = parser.parse_args()

#Assign local variables args values
arg1 = args.arg1
arg2 = args.arg2

print("The first argument was: "+arg1)
print("The second argument was: "+arg2)





