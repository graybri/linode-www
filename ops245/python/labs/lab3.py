#!/usr/bin/env python3
# tarchiver.py
# Purpose: Creates a tar archive of a directory
#
# USAGE: ./tarchiver.py
#
# Author: *** Brian Gray ***
# Date: *** OCT 6th 2021 ***


import os

dirname = input("What is the absolute path of the directory you wish to archive: ")
archname = input("What would you like to call the archive: ")
x=0
y=0

while x == 0:
  ans1 = input("Do you wish to use compression? (y/n) :")

  if ans1 == 'n':
    x = 1
    os.system("tar cvf " + archname + ".tar " + dirname)
  elif ans1 == 'y':
    x = 1
    while y==0: 
      ans2 = input("What compression type? (gzip,bzip,xz) :")
      if ans2=='gzip':
        y=1
        os.system("tar cvzf " + archname + ".tar.gz " + dirname)
      elif ans2=='bzip':
        y=1
        os.system("tar cvjf " + archname + ".tar.bz " + dirname)
      elif ans2=='xz':
        y=1
        os.system("tar cvJf " + archname + ".tar.xz " + dirname)
      else:
        print("Please enter a valid response")
  else:
    print("Please enter 'y' or 'n'")
