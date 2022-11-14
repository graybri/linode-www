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
# Name    : file6.py
#
# Purpose : Demonstrate reading file contents a certain 
#           number of bytes at a time.
#           Demonstrate .tell() method to return current
#           position within the file (pointer)
#           Demonstrate the .seek() method to move to a
#           postion within the file
#
# Usage   : ./file6.py
#           (requires test.txt for demonstration)
#
#######################################################

# We can move through the file contents by reading a 
# certain number of bytes at a time, or by using the 
# .seek() method
# We can see our current position within the file by 
# using the .tell() method

with open('test.txt','r') as fo:
  # read 10 bytes and print
  contents=fo.read(10)
  print(contents)
  
  # print current position
  print(fo.tell())
  print()

  #read another 20 bytes and print
  contents=fo.read(20)
  print(contents)
 
  # print current position
  print(fo.tell())
  print()
  
  # we can use the .seek() method to move through the file
  # fo.seek(offset, whence) 
  # whence 0 means from the beginning of the file 
  # whence 1 means from current position (binary files)
  # whence 2 means from the end of the file (binary files)
  # default whence is 0
  # fo.seek(0) move to begining of the file
  # fo.seek(5) move 5 bytes from the begining
  # fo.seek(5,1) move 5 bytes from current position (binary files)
  # fo.seek(-5,2) move 5 bytes back from the end of the file (binary files)
  
  # Move forward 35 characters from beginning of the file (byte #30)
  fo.seek(35)
  print(fo.tell())
  print()

  # Read another 10 bytes and print position
  contents=fo.read(10)
  print(contents)
  print(fo.tell())
  print()



