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
# Name    : try.py
#
# Purpose : Demonstrate exception handling (error handling) 
#           Using try: ... except:
#
# Usage   : ./try.py	 
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


# Try to print() 2 values of different datatypes

word='hello'
num=42

try:
    # This command will fail because of 2 different datatypes
    print(word + num)
except:
    # This will trap any of the possible exceptions
    print("Some kind of error occurred")

input("Press enter to continue...")

# We can trap specific named exceptions and handle them differently

try:
    # This command will fail because of 2 different datatypes
    print(word + num)
except TypeError:
    # This will trap an exception caused by two different datatypes
    print("Datatypes don't match")
except:
    # This will trap all of the other possible exceptions
    print("Some other kind of error occurred")
else:
    # This block will execute only if no exceptions
    print("It worked!")

input("Press enter to continue...")


