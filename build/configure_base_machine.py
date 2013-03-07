#! /usr/bin/python

from config_file_edit_functions import *

import os, sys

rhn_username = "changeme"
rhn_userpass = "changeme"
reminders = []
#############################################################################
###                                Show Menu                              ###
#############################################################################
def main ():
    # Build a list of menu items
    menu_list = []
    
    # Build a map of all cluster groups
    for profile in config_profiles :
        menu_list.append([profile,"X"])
    pass 

    # the menu loop
    while(1):
        
        # print out the map as a menu
        for i, j in enumerate(menu_list):
                print " ["+j[1]+"]", "%2s"%i, ") "+j[0]

        print "Please select which profiles to apply (l Launches) (q exits) -> "
        
        choice = raw_input()
        
        # leave the results of last iterations on the top
        os.system("clear")
        # exit
        if choice == "q" or choice == "Q":
            print "Don't for get to ....."
        for item in reminders :
            print item
                sys.exit(0)
        # launch
        elif choice == "l" or choice == "L":
            for i, j in enumerate(menu_list):
               if "*" in j[1] :
                   exec "config_"+j[0]+"()"
            pass                                                                  
        # toggle the line selected
        else:
            try :
                chosen = int(choice)
                if "X" in menu_list[chosen][1] :
                    menu_list[chosen][1] = "*"
                else :
                    menu_list[chosen][1] = "X"
                pass
            except Exception as e:
                # Catches any entry that doesn't do something
                print e
                print "Invalid entry please choose again. Press q to exit."
            pass                                    
        pass   
pass

config_profiles = ("base", "vmware","redhat_network")

def config_base() :
    #increase root history retention
    arch_globed_files("/root/.bashrc","y")
    add_to_file("/root/.bashrc","HISTSIZE=10000")
    
    #Turn off security until post build
    arch_globed_files("/etc/selinux/config","y")
    add_unique_entry_to_file("/etc/selinux/config","SELINUX=","SELINUX=disabled")

    #set run level to 3    
    arch_globed_files("/etc/inittab","y")
    replace_all_occurances_of_a_phrase("/etc/inittab","id:5:initdefault:","id:3:initdefault:")

    # add the step tickers for jumps
    arch_globed_files("/etc/ntp/step-tickers","y")
    add_to_file("/etc/ntp/step-tickers", "server 0.rhel.pool.ntp.org")
    add_to_file("/etc/ntp/step-tickers", "server 1.rhel.pool.ntp.org")
    add_to_file("/etc/ntp/step-tickers", "server 2.rhel.pool.ntp.org")
    
    # Force the new time incase the jump is to big
    os.system("service ntpd stop")
    os.system("ntpdate 0.rhel.pool.ntp.org")
    os.system("service ntpd start")


pass


def config_redhat_network():
    print "RHN must be registered manually press any key to proceed (q exits) -> "
            
    choice = raw_input()

    # exit
    if choice == "q" or choice == "Q":
        return

    os.system("rhn_register")        

    print "If rhn_register failed press q to exit -> "

    choice = raw_input()

    # exit
    if choice == "q" or choice == "Q":
        return

    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhel-x86_64-server-supplementary-6")
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhn-tools-rhel-x86_64-server-6")
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhel-x86_64-server-optional-6")
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhel-x86_64-server-ha-6")
pass

    
def config_vmware():
    print "Preping VMWare tools for install"
    os.system("rm -fr /etc/vmware-install")
    try:    
        os.makedirs("/etc/vmware-install")
    #ignore exception thrown if directory exists
    except :        
        pass
    
    os.system("cp /mnt/admin_build_directory/vmware/VMwareTools-*.tar.gz /etc/vmware-install")
    os.system("tar -zxvf /etc/vmware-install/VMwareTools-*.tar.gz -C /etc/vmware-install/")
    print "For safety vmware tools install is kicked off manually (/etc/vmware-install/vmware-tools-distrib/vmware-install.pl)"
    reminders.append("/etc/vmware-install/vmware-tools-distrib/vmware-install.pl")
pass


if __name__ == '__main__': 
    if(rhn_username == "changeme"):
        print "Please initialize the values in "+sys.argv[0]
        sys.exit()
    pass
   
    main()
pass

