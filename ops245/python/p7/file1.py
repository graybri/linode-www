#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

fo=open('test.txt','r')

#print filename and mode

print(fo.name)
print(fo.mode)
contents=fo.read()
print(contents.strip())
# important to  close file
fo.close()
