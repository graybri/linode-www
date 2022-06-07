#!/usr/bin/env python3

#############################################
#   Script:     grouper.py
#   Author:     Brian Gray
#   Usage:      grouper.py <datafile>
#   Date:       2021-12-06
#############################################

#############################################
##               Description                
# 
# Fall 2021 OPS245 Ass 2 script to create
# groups and add users to those supplemental
# groups.
#
# File layout:
# 
# groupname:gid:user1,user2,user3
# 
# a2-sample.txt
# 
# 
#############################################

import argparse
import os

currentuser = os.popen('whoami')
user = currentuser.read()
user = user.strip()
if user != 'root':
  print("You must be root to run this script")
  print("You are currently the user " + user)
  exit()

parser = argparse.ArgumentParser(description='Assign 2: add groups and users')

parser.add_argument('file',help='Enter a datafile name')

args = parser.parse_args()
infile = args.file

with open(infile,'r') as fo:
    lines=fo.readlines()

for line in lines:
    gname,gid,users = line.strip().split(':')
    names=[]
    names=users.split(',')
    if gid:
        os.system('groupadd -g ' + gid + ' ' + gname)
    else:
        os.system('groupadd ' + gname)
                    
    for name in names: 
        os.system('usermod -aG ' + gname + " " + name)


