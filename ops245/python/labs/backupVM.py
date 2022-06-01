#!/usr/bin/env python3

'''
  ____   ____   	Brian Gray
 | __ ) / ___| 	    School of Information Technology
 |  _ \| |  _   	Administration & Security
 | |_) | |_| |_ 	Seneca College
 |____(_)____(_)	brian.gray@senecacollege.ca
'''                
########################################################
# Author  : Brian Gray
# Date    : 2022-05-30
# 
# Name    : backupVM.py
#
# Purpose :	Modified from lab2.py for Assignment 1
#           Dynamically list of VM's with virsh list
#           Dynamically retrieves image filename from
#           virsh dumpxml 
# 
#
#
# Usage   :	 
#
#######################################################

import os

currentuser = os.popen('whoami')
user = currentuser.read()
user = user.strip()
if user != 'root':
  print("You must be root to run this script")
  print("You are currently the user " + user)
  exit()
else:
  vmlist=[]
  vms=os.popen("virsh list --all --name")

  for vm in vms.readlines():
    vmname=vm.strip()
    if vmname!="":
      vmlist.append(vmname)

  ans = input('Do you wish to backup all VM\'s? (y/n) ')
  if ans=='y':
    for machine in vmlist:
      print('Backing up ' + machine)
      command='virsh dumpxml ' + machine + '| grep "source file" | cut -d\\\' -f2' 
      img=os.popen(command)
      imgfile=img.read()
      imgfile=imgfile.strip()
      os.system('gzip < ' + imgfile + ' > ~bgray/backups/' + machine + '.qcow2.gz')
  else:
    machine = input('Which VM would you like to backup? '+str(vmlist) + ': ')
    print('Backing up ' + machine)
    command='virsh dumpxml ' + machine + '| grep "source file" | cut -d\\\' -f2' 
    img=os.popen(command)
    imgfile=img.read()
    imgfile=imgfile.strip()
    os.system('gzip < ' + imgfile + ' > ~bgray/backups/' + machine + '.qcow2.gz')



