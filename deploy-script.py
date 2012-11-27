#!/usr/bin/python

import os

#implies a saved ssh key
#Sync build script with base image
os.system("rsync -avz --delete /home/sysadmin/workspace/linux-admin-toolkit/build/ root@10..10.200:/root/admin/")



