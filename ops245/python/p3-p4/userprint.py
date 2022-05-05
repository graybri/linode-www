#!/usr/bin/env python3

import os

#Get the lines from /etc/passwd for regular users
users=os.popen('grep home /etc/passwd')

'''
users.read() will return the full results of the grep
After the users.read() method users will be empty
causing the loop to print nothing
'''
print(users.read())
print()

for user in users.readlines():
	cutup = user.split(':')
	name = cutup[4]
	uid=cutup[2]
	print(name + ' has UID ' + uid)
