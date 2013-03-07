#! /usr/bin/python

import sys, os, glob, datetime, fileinput

name_server_01 = "changeme"
name_server_02 = "changeme"
nfs_server="changeme:/changeme"
domain_name = "changeme.com"

#############################################################################
###                      Machine Build Functions                          ###
#############################################################################
def main():
    config_network()
    config_domain()
    restart_network()
    mount_nfs_build_directory()
    print "Build complete. Now ...."
    print "1 - Reboot machine (shutdown -r now) to activate new hostname and persist any mac address changes"

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
    remove_from_file("/etc/sysconfig/network-scripts/ifcfg-eth0","GATEWAY")
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

def mount_nfs_build_directory() :
    try:    
        os.makedirs("/mnt/admin_build_directory")
    #ignore exception thrown if directory exists
    except :        
        pass

    os.system("chmod a-w /mnt/admin_build_directory")

#############################################################################
###                      Helper Functions                                 ###
#############################################################################
# archive all files fitting a glob
# if preserve is set to "n" destroy the original. 
def arch_globed_files(glb, preserve):
    now = datetime.datetime.now()
    #create the archive destination if it does not yet exist.
    try:
        os.makedirs("/etc/configuration_file_archive")
    #ignore exception thrown if directory exists
    except :        
        pass
        
    filelist=glob.glob(glb)
    for file in filelist:
        new_location = "/etc/configuration_file_archive/"+os.path.basename(file)+"_"+now.strftime("%Y-%m-%d-%I%M%S%p")        
        if preserve == "n":
            print "archiving -> ", file," to ->", new_location 
            os.system("mv "+file+" "+new_location)
        else:
            print "backing up -> ", file," to ->", new_location 
            os.system("cp "+file+" "+new_location)


#replace all lines containing the phrase searchExp with the complete new line specified in replaceExp.
#Delete the line if replaceExp is blank 
def replace_any_line_containing_word(file,search_exp,replace_exp):
    for line in fileinput.input(file, inplace=1):
        if search_exp in line:            
            if replace_exp:                #we don't even want a blank line if null 
                print replace_exp
        else :
             sys.stdout.write(line)

#wrapper function to delete line containing subtraction in it
def remove_from_file(file, search_exp):
    replace_any_line_containing_word(file,search_exp,"")

#make sure to remove any old occurrences of line and add it to end of file. 
def add_to_file(file, replace_exp):
    remove_from_file(file, replace_exp)
    file_handle = open(file, "a")
    try:
        file_handle.write(replace_exp+"\n")
    finally:
        file_handle.close()    

# add a parameter to a file making sure any old occurrences of the parameter are replaced. 
def add_unique_entry_to_file(file,search_exp,replace_exp):
    remove_from_file(file, search_exp)
    add_to_file(file,replace_exp)

# replace only the characters specified in serach_exp in all places in a file
def replace_all_occurances_of_a_phrase(file,search_exp,replace_exp):    
    for line in fileinput.input(file, inplace=1):
        line = line.replace(search_exp,replace_exp)        
        sys.stdout.write(line)    # using write instead of print, squelches carriage returns


#############################################################################
###                      Start Here                                       ###
#############################################################################
if __name__ == '__main__':
    if(domain_name == "changeme.com"):
        print "Please initialize the values in "+sys.argv[0]
        sys.exit()
    pass


    if(len(sys.argv) != 4) :
        print "Usage: "+sys.argv[0]+" hostname ipaddress_suffix ipaddress_postfix"
        print "Post install steps ...."
        print "1 - mount -t nfs "+nfs_server+" /mnt/admin_build_directory -o intr"
        print "2 - cd /mnt/admin_build_directory"
        sys.exit()
    else :
        main()
    pass

pass
