#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

### Alternate method no need to close
### Using context manager with block
### file automatically closed when block ends

print("enter block")

with open('test.txt','r') as fo:
  print(fo.mode)
  print(fo.name)
  # read contents of file to variable
  fo_contents=fo.read()
  print(fo_contents)
  #see file is not closed
  print(fo.closed)

#exit block
print("exit block")
print(fo.mode)
#see file is closed after block ends
print(fo.closed)




