#!/usr/bin/env python3

'''
Purpose: countup.py
This is a simple python script demonstrating reversing a condition
Note that the loop could be done with counter != 10
This is just done this way to demonstrate how comparing a condition to a boolean can work.

Author: Peter Callaghan
Date: 05 Feb. '21

'''

# Initialze counter to int value 0
counter=0

# Check a condition and see if it is False
while (counter == 10) == False:
  print(counter)
# Increment counter
  counter+=1

print(counter)
