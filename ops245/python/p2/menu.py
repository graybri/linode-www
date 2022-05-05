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
# Date    : 2022-05-03
# 
# Name    : menu.py
#
# Purpose :	Demonstrate a script to present menu and 
#           accept user input of menu selection, but
#           with no conditional logic not functional
#           Demonstrate import os, input(), os.system()
#
# Usage   :	./menu/py 
#
#######################################################

# Import os module
import os

# Display menu
print("To help us direct your call, please select a department:")

print("For accounting, press 1.")
print("For human resources, press 2.")
print("For public relations, press 3.")
print("For collections, press 4.")
print("For complaints, press 5.")

# Accept user input for menu choice
ans = input('')

# Display feedback messages to user
# Use os.system() to pause 3 secs between messages
print("You pressed " + ans + ".")
os.system('sleep 3')
print("We're sorry, no one from that department is available to take your call.")
os.system('sleep 3')
print("Please call again. Good-bye")
