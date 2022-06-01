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
# Date    : 2022-05-18
# 
# Name    : lab2.py
#
# Purpose :	Backs up centosX VM's
#           Establish root access
#           Backup individual VM's or ALL
# 
# Usage   :	./lab2.py 
#
#######################################################

# Import OS module
import os

# Get current username (looking for root)
# Use os.popen() to get username, assign to object currentuser
currentuser = os.popen('whoami')
# Use .read() method to return contents of currentuser as string
# assign to string object user
user = currentuser.read()
# Use strip() method on user to strip any whitespace
user = user.strip()

# Test for user root, display error and exit()
if user != 'root':
  print("You must be root to run this script")
  print("You are currently the user " + user)
  exit()

# If root prompt user for VM's to backup all or one of centos1,centos2,centos3
else:
  ans = input('Do you wish to backup all VM\'s? (y/n) ')
  if ans=='y':
    for machine in {'centos1','centos2','centos3'}:
      print('Backing up ' + machine)
      os.system('gzip < /var/lib/libvirt/images/' + machine + '.qcow2 > ~bgray/backups/' + machine + '.qcow2.gz')
  else:
    machine = input('Which VM would you like to backup? (centos1,centos2,centos3) ')
    print('Backing up ' + machine)
    os.system('gzip < /var/lib/libvirt/images/' + machine + '.qcow2 > ~bgray/backups/' + machine + '.qcow2.gz')



