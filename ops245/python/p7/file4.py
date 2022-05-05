#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

### Not always practical to use fo.read() method
### Working with the entire contents of the file at once
### Often better to read in contents of the file a line at a time

with open('test.txt','r') as fo:
  # read the next line of the file fo.readline() which returns a single line
  fo_contents=fo.readline()
  fo_contents=fo_contents.strip()
  print(fo_contents)




