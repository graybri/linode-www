#!/usr/bin/env python3

'''
This script will demonstrate a while loop that includes an else: block.
The else: block will execute when the condition evaluates to false
'''

import os

count=10

while count > 0:
	print("--> " + str(count))
	os.system('sleep 1')
	count=count-1
else:
	print("Blast Off!!")


