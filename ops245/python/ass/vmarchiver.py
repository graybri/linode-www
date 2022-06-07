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
# Name    : vmarchiver.py
#
# Purpose :	Modified from backupVM.py for Assignment 1
#           Dynamically list of VM's with virsh list
#           Dynamically retrieves image filename from
#           virsh dumpxml 
#
# Usage   :	./vmarchiver (as root) 
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
    
  machine=''
  while machine not in vmlist: 
    machine = input('Which VM would you like to backup? '+str(vmlist) + ': ')
  
  print('Backing up ' + machine)
  xmlcommand='virsh dumpxml ' + machine + ' >> /var/lib/libvirt/images/' + machine + '.xml'
  os.system(xmlcommand) 
  imgcommand='virsh dumpxml ' + machine + '| grep "source file" | cut -d\\\' -f2' 
  img=os.popen(imgcommand)
  imgfile=img.read()
  imgfile=imgfile.strip()
  date=os.popen('date +%Y%m%d')
  today=date.read()
  today=today.strip()
  tarcommand='tar cvJf /home/bgray/backups/' + machine + '-' + today + '.tar.xz ' + imgfile + ' /var/lib/libvirt/images/' + machine + '.xml' 
  os.system(tarcommand)



