#!/usr/bin/env python3

'''
Purpose: countup.py
This is a simple python script demonstrating reversing a condition with not
Note that the loop could be done with counter != 10

Author: Peter Callaghan
Date: 05 Feb. '21
'''

counter=0

# add the 'not' keyword before the condition to invert the result
while not(counter == 10):
  print(counter)
  counter+=1

print(counter)
