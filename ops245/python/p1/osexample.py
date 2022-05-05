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
# Date    : 2022-04-27
# 
# Name    : osexample.py
#
# Purpose :	Demonstrate importing python modules
#           Demonstrate use of os.system()
#           Demonstrate use of os.popen()
#           Demonstrate use of var.read() method
#
# Usage   :	./osxample.py 
#
#######################################################

# Import the os module making its functions and methods 
# available.
# os module provides functions for interacting with 
# operating system commands

import os

# Use os.system() to execute an OS command 
# and output result to STDOUT
# os.system() returns the exit status of the command which 
# can be assigned to a variable

flag=os.system('uname -rv')

# Display the datatype of the flag variable (int)
print(type(flag))

# Display a message with the exit status
# Note the use of the str() function to convert the 
# the datatype to string so that the + operator works

print('Exit Status: ' + str(flag))
print()

# Use os.popen() to execute an OS command and return 
# the output of the command instead of displaying it.
# That output can be assigned to a variable.

output=os.popen('hostname')

# Display the special data type of the variable(object) that 
# contains the output of the previous command.

print(type(output))

# Display the contents of the output object using the
# object.read() method
# output.read() will return the contents of output as a string 

print(output.read())



