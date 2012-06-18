#!/usr/bin/python

import os

#implies a saved ssh key

# deploy our application
os.system("rsync -avz --delete /home/sysadmin/git/linux-admin-toolkit root@192.168.30.144:/u01/admin/")

# over write the dummy values
os.system ("rsync -avz /tmp/local-config root@192.168.30.144:/u01/admin/linux-admin-toolkit/")


