#!/usr/bin/env python3

import argparse


#instantiate the parser object
parser = argparse.ArgumentParser(description='Sample argparse usage')

#Add positional arguments (required postional arguments)
parser.add_argument('num1', help='Enter the 1st number', type=int)
parser.add_argument('num2', help='Enter the 2nd number', type=int)

#Add options into mutually exclusive group)
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--add', help="option for addition", action="store_true")
group.add_argument('-s', '--subtract', help="option for subtraction", action="store_true")
group.add_argument('-m', '--multiply', help="option for multiplication", action="store_true")

#Parse the command line and assign arguments to args
args = parser.parse_args()

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


