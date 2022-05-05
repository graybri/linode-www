#!/usr/bin/env python3

# Demo of try: except: finally:

# prompt for filename
file=input('Enter a filename: ')


# start try: block
try:
  fo=open(file, "r+")
  content=fo.read()
  print('Contents : ' + content)
  fo.close()
except:
  print('Invalid Filename')
finally:
  print('thanks')








