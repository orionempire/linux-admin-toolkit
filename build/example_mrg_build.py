#! /usr/bin/python

from config_file_edit_functions import *
import config_file_edit_functions

import os
#############################################################################
###                      MRG Build Functions                          ###
#############################################################################
def main():
    config_file_edit_functions.base_archive_directory = "/mnt/admin_build_directory/"    
    config_file_edit_functions.default_file_owner="mrgadmin"
    do_initial()
    do_qpidd_conf()
    do_cumin_conf()
    do_my_acl()
    do_iniitalize_service()
    do_load_user_passwd()
    do_create_rmg_q()
    
    
def do_initial():
    os.system("useradd "+config_file_edit_functions.default_file_owner)
    log_item("REMEMBER","Set "+config_file_edit_functions.default_file_owner+" password")
    log_item("REMEMBER","Set "+config_file_edit_functions.default_file_owner+" sudo")

# Step 2 - Edit /etc/qpidd.conf
def do_qpidd_conf() :
    arch_globed_files("/etc/qpidd.conf","y")
    add_unique_entry_to_file("/etc/qpidd.conf","cluster-mechanism","cluster-mechanism=ANONYMOUS")
    add_unique_entry_to_file("/etc/qpidd.conf","port","port=15726")
    add_unique_entry_to_file("/etc/qpidd.conf","log-time","log-time=yes")
    add_unique_entry_to_file("/etc/qpidd.conf","trace","trace=no")
    add_unique_entry_to_file("/etc/qpidd.conf","worker-threads","worker-threads=20")
    add_unique_entry_to_file("/etc/qpidd.conf","auth","auth=yes")
    add_unique_entry_to_file("/etc/qpidd.conf","default-queue-limit","default-queue-limit=524288000")
    add_unique_entry_to_file("/etc/qpidd.conf","heartbeat","heartbeat=10")
    add_unique_entry_to_file("/etc/qpidd.conf","mgmt-pub-interval","mgmt-pub-interval=1")
    add_unique_entry_to_file("/etc/qpidd.conf","mgmt-enable","mgmt-enable=yes")
    
# Step 3 - Edit /etc/cumin/cumin.conf
def do_cumin_conf() :
    arch_globed_files("/etc/cumin/cumin.conf","y")
    add_unique_entry_to_file("/etc/cumin/cumin.conf","brokers:","brokers: cumin/cumin@localhost:15726")
    add_unique_entry_to_file("/etc/cumin/cumin.conf","sasl-mech-list","sasl-mech-list=PLAIN")
    
def do_my_acl():
    deploy_files("my.acl","mrg/my_acl/","/home/mrgadmin/","n")
    
def do_iniitalize_service():
    os.system("service qpidd restart")
    os.system("service cumin restart")
    os.system("cumin-database start")
    os.system("cumin-admin upgrade-schema")
    os.system("service cumin restart")
    
def do_create_rmg_q():
    deploy_files("createMrgQ.py","mrg/create_mrg_q/","/home/mrgadmin/","n")    
    os.system("chmod a+x /home/mrgadmin/createMrgQ.py")
    os.system("/home/mrgadmin/createMrgQ.py")
    
def do_load_user_passwd():
    deploy_files("*","mrg/load_user_passwd/","/home/mrgadmin/","n")    
    os.system("chmod a+x /home/mrgadmin/addMrgUsers.sh")    
    os.system("/home/mrgadmin/addMrgUsers.sh /home/mrgadmin/UserPass.csv")
    
if __name__ == '__main__':       
    main()
pass
