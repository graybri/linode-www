#!/usr/bin/env python3

import os
vmlist=[]

vms=os.popen("virsh list --all --name")

for vm in vms.readlines():
  vmname=vm.strip()
  if vmname!="":
    vmlist.append(vmname)
    print(vmname)

print(vmlist)
