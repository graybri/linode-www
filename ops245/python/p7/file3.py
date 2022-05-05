#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

### Not always practical to use fo.read() method
### Working with the entire contents of the file at once
### Often better to read in contents of the file a line at a time

with open('test.txt','r') as fo:
  # read contents of file to variable using fo.readlines() which returns a list of lines
  fo_contents=fo.readlines()
  print(fo_contents)




