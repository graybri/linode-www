#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

### Not always practical to use fo.read() method
### Working with the entire contents of the file at once
### Often better to read in contents of the file a line at a time

with open('test.txt','r') as fo:
  # loop through the lines one at a time and print
  for line in fo:
    line=line.strip()
    print("The line is: " + line)




