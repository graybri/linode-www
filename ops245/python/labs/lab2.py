#!/usr/bin/env python3

# backupVM.py
# Purpose: Backs up virtual machines
#
# USAGE: ./backupVM.py
#
# Author: *** Brian Gray ***
# Date:   *** Sept 29/2021 ***

import os

currentuser = os.popen('whoami')
user = currentuser.read()
user = user.strip()
if user != 'root':
  print("You must be root to run this script")
  print("You are currently the user " + user)
  exit()
else:
  ans = input('Do you wish to backup all VM\'s? (y/n) ')
  if ans=='y':
    for machine in {'centos1','centos2','centos3'}:
      print('Backing up ' + machine)
      os.system('gzip < /var/lib/libvirt/images/' + machine + '.qcow2 > ~bgray/backups/' + machine + '.qcow2.gz')
  else:
    machine = input('Which VM would you like to backup? (centos1,centos2,centos3) ')
    print('Backing up ' + machine)
    os.system('gzip < /var/lib/libvirt/images/' + machine + '.qcow2 > ~bgray/backups/' + machine + '.qcow2.gz')



