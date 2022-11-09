#!/usr/bin/env python3
#
#  ____   ____   	Brian Gray
# | __ ) / ___| 	School of Information Technology
# |  _ \| |  _   	Administration & Security
# | |_) | |_| |_ 	Seneca College
# |____(_)____(_)	brian.gray@senecacollege.ca
#                

########################################################
# Author  : Brian Gray
# Date    : 2022-08-10
# 
# Name    : try2.py
#
# Purpose : Demonstrate exception handling (error handling)
#           For opening of files 
#           Trap and handle various exceptions
#           Using try: ... except:
#           Run with readonly file (test.ro)
#           Run with missing file (test.rw)`
#
# Usage   : ./try2.py	 
#
#######################################################

# Some operations that we peform within our script may 
# fail because of some sort of error outside of the script.
# For example; opening a database connection, opening a file etc.
# These actions can fail for various reasons eg persmissions 
# To trap and handle these errors (exceptions) we can run them 
# within a try: block
# Then we can test for all exceptions or specific exceptions 
# with a except <exceptionname>: block
# We can add an else block for what to do if no exception occurs

# Prompt for filename
file=input('Enter a filename: ')

# start try: block
try:
    # Attempt to open file in Read/Write mode
    fo=open(file, "r+")
except PermissionError:
    # This will handle file permission exception
    print("You do not have permission to this file")
except FileNotFoundError:
    # This will handle file not found exception
    print("This file does not exist")
except:
    # This will handle all other exceptions
    print("Error Opening File")
else:
    # Do this if file opened successfully
    content=fo.read()
    print('Contents : ' + content)
    fo.close()
finally:
  print('thanks')








