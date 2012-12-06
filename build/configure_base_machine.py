#! /usr/bin/python
import os, sys

rhn_username = "changeme"
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

config_profiles = ("base", "vmware")

def config_base():
    print "RHN must be registered manually (rhn_register) press any key to proceed (q exits) -> "
        
    choice = raw_input()

    # exit
    if choice == "q" or choice == "Q":
        sys.exit(0)
    
    print "Enter rhn password for user "+rhn_username+" -> "
    rhn_userpass = raw_input()
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhel-x86_64-server-supplementary-6")
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhn-tools-rhel-x86_64-server-6")
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhel-x86_64-server-optional-6")
    os.system("rhn-channel -a -u "+rhn_username+" -p "+rhn_userpass+" -c rhel-x86_64-server-ha-6")
pass

    
def config_vmware():
    print "Installing VMWare tools"
    #select install guest additions.
    os.system("mkdir /mnt/cdrom")
    os.system("mount /dev/cdrom /mnt/cdrom")
    os.system("cd /etc/vmware-install")
    os.system("rm -fr /tmp/VMwareTools*")
    os.system("cp /mnt/cdrom/VMwareTools-*.tar.gz /etc/vmware-install/")
    os.system("tar -zxvf /etc/vmware-install/VMwareTools-*.tar.gz -C /etc/vmware-install/")
    os.system("umount /dev/cdrom")
    print "Now run the configuration wizard"
pass


if __name__ == '__main__': 
    if(rhn_username == "changeme"):
        print "Please initialize the values in "+sys.argv[0]
        sys.exit()
    pass
   
    main()
pass