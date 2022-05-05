#!/usr/bin/env python3

# open file and create file object fo
# Modes include r,a,w,r+,a+


try:
	with open('missing.txt','r') as fo:
		for line in fo:
			print(line.strip())
except FileNotFoundError:
	print("File not found")
except:
	print("Other file error")



try:
	with open('testro.txt','w') as fo:
  		fo.write("new line of text\n")
except PermissionError:
	print("No write permission")
except:
	print("Other file error")






