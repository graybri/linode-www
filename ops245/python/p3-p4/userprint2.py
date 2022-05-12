#!/usr/bin/env python3

'''
____   ____       Brian Gray
| __ ) / ___|      School of Information Technology
|  _ \| |  _       Administration & Security
| |_) | |_| |_     Seneca College
|____(_)____(_)    brian.gray@senecacollege.ca
'''
########################################################
# Author  : Brian Gray
# Date    : 2022-05-11
# 
# Name    : userprint2.py
#
# Purpose : Demonstrate the use of os.popen()
#           os.popen() returns the output of an OS 
#           command as a special object.
#           Demonstrate the use of readlines() method
#           to return the contents of the obect as a 
#           list of lines
#           Loop through a list of lines
#           Demonstrate the split() method to split 
#           fields from a line into a list
#           Demonstrate accessing list values by index
#
# Usage   : ./userprint.py 
#
#######################################################

# Import the os module which provides the popen() function
import os

# Use os.popen() to retrieve the relevant lines from
# /etc/passwd
# Assign the output of the command to the object users
users=os.popen('grep home /etc/passwd')

# Comment out the users.read()
#print(users.read())
#print()

# users.readlines() will return the results of the grep 
# command as a list of lines, allowing us to loop through 
# the lines one at a time, split them into a list on the
# : character and then build a new line of output using 
# just the full name and UID from the list using the index
for user in users.readlines():
	cutup = user.split(':')
	name = cutup[4]
	uid=cutup[2]
	print(name + ' has UID ' + uid)
