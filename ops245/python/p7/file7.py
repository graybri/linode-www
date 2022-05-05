#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+

with open('test.txt','r') as fo:
	print("**old contents**")
	for line in fo:
		print(line.strip())
	print()

with open('test.txt','w') as fo:
  fo.write("new line of text\n")
  fo.write("another new line\n")

with open('test.txt','r') as fo:
	print("new contents")
	for line in fo:
		print(line.strip())
	print()

with open('test.txt','a') as fo:
  fo.write("add new line to the end\n")
  fo.write("add another new line to the line\n")


with open('test.txt','r') as fo:
	print("newest contents")
	for line in fo:
		print(line.strip())
	print()






