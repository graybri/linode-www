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
#
# Date    : 2022-11-13
# 
# Name    : file8.py
#
# Purpose : Demonstrate opening the file within a try:
#           block to trap common exceptions
#
# Usage   : ./file8.py
#           (requires the readonly file testro.txt )
#           (requires the file missing.txt to be missing)
#
#######################################################

# OS filesystem errors are quite possible when working 
# with files.
# File not found and Permission exceptions should be
# handled correctly within our scripts.
# Files should be opened within a try: except: block
# to handle exceptions

# Open the file in with: block within try: block
try:
    with open('missing.txt','r') as fo:
        for line in fo:
            print(line.strip())

# Use except block to trap FileNotFoundError exception
except FileNotFoundError:
    print("File not found")

# Use except block to trap  other exceptions
except:
    print("Other file error")


# Open the file in with: block within try: block
try:
    with open('testro.txt','w') as fo:
        fo.write("new line of text\n")

# Use except block to trap PermissionError exception
except PermissionError:
    print("No write permission")

# Use except block to trap  other exceptions
except:
    print("Other file error")



