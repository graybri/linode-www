#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

with open('test.txt','r') as fo:
  #read 30 bytes and print
  contents=fo.read(10)
  print(contents)

  print(fo.tell())


  #read another 30 bytes and print
  contents=fo.read(10)
  print(contents)
 
  print(fo.tell())
  
  # fo.seek(offset, whence) 
  # whence 0 means from the beginning of the file 
  # whence 1 means from current position (binary files)
  # whence 2 means from the end of the file (binary files)
  # default whence is 0
  # fo.seek(0) move to begining of the file
  # fo.seek(5) move 5 bytes from the begining
  # fo.seek(5,1) move 5 bytes from current position (binary files)
  # fo.seek(-5,2) move 5 bytes back from the end of the file (binary files)
  
  # Move forward 30 characters from beginning of the file
  fo.seek(30)
  print(fo.tell())

  contents=fo.read(10)
  print(contents)
  print(fo.tell())
  



