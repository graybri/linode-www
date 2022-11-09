#!/usr/bin/env python3
# tarchiver2.py
# Purpose: Creates a tar archive of a directory
#
# USAGE: ./tarchiver2.py
#
# Author: *** Brian Gray ***
# Date: *** OCT 6th 2021 ***


import os
import argparse

parser=argparse.ArgumentParser(description='Archives a directory')
parser.add_argument('dirname', help='enter the directory path', type=str)
parser.add_argument('archname', help='enter the archive name', type=str)
group=parser.add_mutually_exclusive_group()
group.add_argument('-g','--gz', help="Option for gzip compression", action="store_true")
group.add_argument('-b','--bz', help="Option for bzip compression", action="store_true")
group.add_argument('-x','--xz', help="Option for x compression", action="store_true")

args=parser.parse_args()

dirname=args.dirname
archname=args.archname

if args.gz:
  os.system("tar cvzf " + archname + ".tar.gz " + dirname)
elif args.bz:
  os.system("tar cvjf " + archname + ".tar.bz " + dirname)
elif args.xz:
  os.system("tar cvJf " + archname + ".tar.xz " + dirname)
else:
  os.system("tar cvf " + archname + ".tar " + dirname)
