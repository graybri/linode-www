#!/usr/bin/env python3

# Demo of not using try: except: finally:


#prompt for filename

file=input('Enter a filename: ')

# open file for reading creating a filehandle object
fo=open(file, "r+")

# read in contents of the file
content=fo.read()

# output contents

print('Contents : ' + content)

# close file
fo.close()

print('thanks')








