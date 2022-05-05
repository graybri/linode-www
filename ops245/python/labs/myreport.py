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
# Date    : 2022-04-29
# 
# Name    : lab1.py
#
# Purpose :	Gather System Info into a report
#           Demonstrate use of os.system() os.popen()
#
# Usage   :	./lab1.py > ~/bin/pythonreport.txt 
#
#######################################################

# Import os module
import os

# Report title
print("**** SYSTEM REPORT ****")
print()

# Output date/time
os.system("date +'%A %B %d, %Y (%I:%M %p)'")
print()

# Run os hostname command and save to object hname
hname=os.popen('hostname')

# Use hname.read() method to ouput contents of
# hname object
print('The hostname is: ' + hname.read())
print()

# Run os uname command and save to object kernel
kernel=os.popen('uname -rv')
print('The kernel version is: ' + kernel.read())
print()

# Run os ip address show command and save to object ifcfg
ifcfg=os.popen('ip address show')
print('The network configuration is:')
print()
print(ifcfg.read())



