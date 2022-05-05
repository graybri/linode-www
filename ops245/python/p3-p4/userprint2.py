#!/usr/bin/env python3

import os

#Get the lines from /etc/passwd for regular users
users=os.popen('grep home /etc/passwd')

'''
users.read() will return the full results of the grep
After the users.read() method users will be empty
causing the loop to print nothing
'''
#comment out the users.read()
#print(users.read())
#print()

'''
users.readlines() will return the results of the grep command as a list of lines
allowing us to loop through the lines one at a time, split into a list on the : character
and then build a new line of output using just the full name and UID from the list
'''
 
for user in users.readlines():
	cutup = user.split(':')
	name = cutup[4]
	uid=cutup[2]
	print(name + ' has UID ' + uid)
