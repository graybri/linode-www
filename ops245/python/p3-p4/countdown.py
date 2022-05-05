#!/usr/bin/env python3

'''
This script will show that we can add an else: block to a for loop.
The else: block will execute after the final iteration of the loop
'''

import os

countdown=['10','9','8','7','6','5','4','3','2','1']

for count in countdown:
	print("--> " + count)
	os.system('sleep 1')
else:
	print("Blast Off!!")


