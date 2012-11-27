#! /usr/bin/python
import sys, os, glob, datetime, fileinput

from config_file_edit_functions import *

name_server_01 = "192.168.X.X"
name_server_02 = "192.168.X.X"
domain_name = "changeme.com"
archive_directory = "/etc/configuration_file_archive/"


#############################################################################
###                      Machine Build Functions                          ###
#############################################################################
def main():
    config_network()
    config_domain()
    restart_network()
    config_preferences()
    set_runlevel()
    set_time()
    print "Build complete. Now ...."
    print "1 - Register with rhn (rhn_register)"
    print "2 - Update the machine (yum update)"
    print "3 - Set the system profile (TBD)"
pass
    
def config_network():
    # remove the phantom NIC, that wa created in the vm copy, by deleting the udev cache.
    arch_globed_files("/etc/udev/rules.d/70-persistent-net.rules","n")
    #backup and then edit ifcfg-eth0
    arch_globed_files("/etc/sysconfig/network-scripts/ifcfg-eth0","y")
    add_unique_entry_to_file("/etc/sysconfig/network-scripts/ifcfg-eth0","IPADDR","IPADDR="+sys.argv[2]+"."+sys.argv[3])
    add_unique_entry_to_file("/etc/sysconfig/network-scripts/ifcfg-eth0","NETMASK","NETMASK=255.255.255.0")
    add_unique_entry_to_file("/etc/sysconfig/network-scripts/ifcfg-eth0","ONBOOT","ONBOOT=yes")
    add_unique_entry_to_file("/etc/sysconfig/network-scripts/ifcfg-eth0","BOOTPROTO","BOOTPROTO=none")
    remove_from_file("/etc/sysconfig/network-scripts/ifcfg-eth0","HWADDR")
    add_unique_entry_to_file("/etc/sysconfig/network-scripts/ifcfg-eth0","NM_CONTROLLED","NM_CONTROLLED=no")
    
pass
    
def config_domain():
     #backup and then edit /etc/hosts
    arch_globed_files("/etc/hosts","y")
    add_unique_entry_to_file("/etc/hosts", sys.argv[2]+"."+sys.argv[3],  
                                          sys.argv[2]+"."+sys.argv[3]+"\t"+sys.argv[1]+".thejavelin.com"+"\t"+sys.argv[1])

    #backup and then edit /etc/sysconfig/network
    arch_globed_files("/etc/sysconfig/network","y")
    add_unique_entry_to_file("/etc/sysconfig/network", "HOSTNAME", "HOSTNAME="+sys.argv[1]+"."+domain_name)
    add_unique_entry_to_file("/etc/sysconfig/network", "GATEWAY", "GATEWAY="+sys.argv[2]+".1")
    
    #add DNS
    arch_globed_files("/etc/resolv.conf","y")
    add_to_file("/etc/resolv.conf","search "+domain_name)
    add_to_file("/etc/resolv.conf","nameserver "+name_server_01)
    add_to_file("/etc/resolv.conf","nameserver "+name_server_02)
    
pass

def restart_network() :
    #restart network
    os.system("chkconfig NetworkManager off")
    os.system("chkconfig network on")
    os.system("service NetworkManager stop")
    os.system("service network restart")
pass

def config_preferences():
    # Maximize root history
    arch_globed_files("/root/.bashrc","y")
    add_to_file("/root/.bashrc","HISTSIZE=10000")
    
    #Turn off security until post build
    arch_globed_files("/etc/selinux/config","y")
    add_unique_entry_to_file("/etc/selinux/config","SELINUX=","SELINUX=disabled")
    
def set_runlevel():
    arch_globed_files("/etc/inittab","y")
    replace_all_occurances_of_a_phrase("/etc/inittab","id:5:initdefault:","id:3:initdefault:")

def set_time():
    # add the step tickers for jumps
    arch_globed_files("/etc/ntp/step-tickers","y")
    add_to_file("/etc/ntp/step-tickers", "server 0.rhel.pool.ntp.org")
    add_to_file("/etc/ntp/step-tickers", "server 1.rhel.pool.ntp.org")
    add_to_file("/etc/ntp/step-tickers", "server 2.rhel.pool.ntp.org")
    
    # Force the new time incase the jump is to big
    os.system("service ntpd stop")
    os.system("ntpdate 0.rhel.pool.ntp.org")
    os.system("service ntpd start")
    

#############################################################################
###                      Start Here                                       ###
#############################################################################
if __name__ == '__main__':
    if(domain_name == "changeme.com"):
        print "Please initialize the values in "+sys.argv[0]
        sys.exit()
    pass

    if(len(sys.argv)) != 4:
        print "Usage: "+sys.argv[0]+" hostname ipaddress_suffix ipaddress_postfix"
        sys.exit()
    pass

    main()
pass
