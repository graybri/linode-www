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
# Date    : 2022-05-11
# 
# Name    : userprint.py
#
# Purpose :	Demonstrate the use of os.popen()
#           os.popen() returns the output of an OS 
#           command as a special object.
#           Demonstrate the use of read() method to 
#           return the contents of the object.
#
# Usage   :	./userprint.py 
#
#######################################################

# Import the os module which provides the popen() function
import os

# Use os.popen() retrieve the relevant lines from
# /etc/passwd
# Assign the output of the command to the object users
users=os.popen('grep home /etc/passwd')

# users.read() will return the full results of the grep
# After the users.read() method users will be empty
# causing the loop to print nothing
print(users.read())
print()

# This loop will print nothing
# The readlines() method will not return any lines as 
# the users object was emptied by the previous read() 
# method.
# For comments about this loop see userprint2.py
for user in users.readlines():
	cutup = user.split(':')
	name = cutup[4]
	uid=cutup[2]
	print(name + ' has UID ' + uid)
