#!/usr/bin/env python3

# vmarchiver.py
# Purpose: Backs up virtual machines
#
# USAGE: ./vmarchiver.py
#
# Author: *** Brian Gray   ***
# Date:   *** June 28/2022 ***

# Import os module
import os

# Test for root
currentuser = os.popen('whoami')
user = currentuser.read()
user = user.strip()
if user != 'root':
  print("You must be root to run this script")
  print("You are currently the user " + user)
  exit()

# Build vmlist
vmlist=[]
vms=os.popen("virsh list --all --name")

for vm in vms.readlines():
  vmname=vm.strip()
  if vmname!="":
    vmlist.append(vmname)

# Prompt for target vm
machine = input('Which VM would you like to backup? '+str(vmlist) + ': ')

while machine not in vmlist:
  print("Please enter a VM from the list...")
  machine = input('Which VM would you like to backup? '+str(vmlist) + ': ')
  
# Retrieve qcow2 filename
command='virsh dumpxml ' + machine + '| grep "source file" | cut -d\\\' -f2' 
img=os.popen(command)
imgfile=img.read().strip()

# Generate xmlfile name
xmlfile='/tmp/' + machine + '.xml'

# Generate xml file
command='virsh dumpxml ' + machine + ' > ' + xmlfile
os.system(command)

# Generate tarfile name
date=os.popen('date +%Y%m%d')
date=date.read().strip()
tarfile='~/backups/' + machine + '-' + date + '.tar.gz' 

# Perform tar backup
command='tar cvzf ' + tarfile + ' ' + imgfile + ' ' + xmlfile
print('Backing up : ' + machine)
os.system(command)
print("DONE")
