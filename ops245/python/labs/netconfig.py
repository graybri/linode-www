#!/usr/bin/env python3

import os

currentuser = os.popen('whoami')
user = currentuser.read()
user = user.strip()
if user != 'root':
  print("You must be root to run this script")
  print("You are currently the user " + user)
  exit()

lines=[]

name=''
while name=='':
	name=input("Enter interface name: ")

lines.append('NAME='+name+'\n')
lines.append('DEVICE='+name+'\n')
#filename=('/etc/sysconfig/network-scripts/ifcfg-'+name)
filename=('ifcfg-'+name)

hwaddr=''
while len(hwaddr)!=17: 
	hwaddr=input("Enter ethernet address: ")

lines.append('HWADDR='+hwaddr+'\n')

onboot=''
while onboot not in ['yes','no']:
	onboot=input("onboot (yes|no): ")

lines.append('ONBOOT='+onboot+'\n')

bootproto=''
while bootproto not in ['static','dhcp']:
	bootproto=input("dhcp or static: ")

lines.append('BOOTPROTO='+bootproto+'\n')

if bootproto=="static":
	ipaddr=''
	while ipaddr=='':
		ipaddr=input("IP Address: ")
	lines.append('IPADDR='+ipaddr+'\n')

	prefix=''
	while prefix not in ['8','16','24']:
		prefix=input("Length of subnet mask: ")
	lines.append('PREFIX='+prefix+'\n')

	gateway=''
	while gateway=='':
		gateway=input("Gateway address: ")
	lines.append('GATEWAY='+gateway+'\n')

	dns1=''
	while dns1=='':
		dns1=input("Primary DNS address: ")
	lines.append('DNS1='+dns1+'\n')
try:
	with open(filename,'w') as outfile:
		for line in lines:
			outfile.write(line)
except:
	print("ERROR: Unable to write to output file")





