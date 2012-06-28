#! /usr/bin/python
'''
Created on Jun 14, 2012

@author: David Davidson

Assumption : 
'''
#modules part of default python library
import os,sys
#modules installed by os (yum or apt-get)
import MySQLdb          #@UnresolvedImport
# Modules installed with EasyInstall 
from configobj import ConfigObj #@UnresolvedImport

#config_path = os.path.abspath(__file__+"/../../../local-config/")
config_path = "/etc/linux-admin-toolkit/config_files/"

# load configuration data
dbconfig = ConfigObj(config_path+"database_config.dat")

# build the file /etc/clusters based on the database
def build_cluster() :
    
    # connect to the database using values in the config file
    database_connection = MySQLdb.connect(dbconfig['database_host'],dbconfig['database_user'], dbconfig['database_pass'],dbconfig['database_schema'])
    
    print("Accessing database....")
    
    with database_connection:
        
        cursor = database_connection.cursor()

        # get a list of all of the unique values in admin_cluster_grouping_1
        cursor.execute("select DISTINCT admin_cluster_grouping_1 from \
        virtual_machine_list union select DISTINCT admin_cluster_grouping_1 from physical_machine_list;")
        admin_cluster_grouping_1_rows = cursor.fetchall()        
        
        # get a list of all of the unique values in admin_cluster_grouping_2
        cursor.execute("select DISTINCT admin_cluster_grouping_2 from virtual_machine_list \
         union select DISTINCT admin_cluster_grouping_2 from physical_machine_list;")
        admin_cluster_grouping_2_rows = cursor.fetchall()        
        
        # create a list of all servers in the database as a cache        
        cursor.execute("select primary_ip, admin_cluster_grouping_1, admin_cluster_grouping_2 \
        from virtual_machine_list union select primary_ip, admin_cluster_grouping_1, admin_cluster_grouping_2 from physical_machine_list;")
        master_server_list_rows = cursor.fetchall()
        
        # create a list of all physical servers in the database as a cache        
        cursor.execute("select primary_ip, admin_cluster_grouping_1, admin_cluster_grouping_2 from physical_machine_list;")
        physical_server_list_rows = cursor.fetchall()
        
        # create a list of all virtual servers in the database as a cache        
        cursor.execute("select primary_ip, admin_cluster_grouping_1, admin_cluster_grouping_2 from virtual_machine_list;")
        virtual_server_list_rows = cursor.fetchall()
        
        print("Building Cluster file....")                
        try:
            file_handle = open("/etc/clusters","w")
            # add a entry to  the cluster files containing every server
            current_cluster_group = "all_servers "
            for counter in range(len(master_server_list_rows)) :
                current_cluster_group += "%1s " % master_server_list_rows[counter][0]
            pass        
            file_handle.write(current_cluster_group + "\n\n")
            
            # add a entry to  the cluster files containing every physical server
            current_cluster_group = "physical_servers "
            for counter in range(len(physical_server_list_rows)) :
                current_cluster_group += "%1s " % physical_server_list_rows[counter][0]
            pass        
            file_handle.write(current_cluster_group + "\n\n")
            
            # add a entry to  the cluster files containing every virtual server
            current_cluster_group = "virtual_servers "
            for counter in range(len(virtual_server_list_rows)) :
                current_cluster_group += "%1s " % virtual_server_list_rows[counter][0]
            pass        
            file_handle.write(current_cluster_group + "\n\n")
                      
            # Write a entry for every distinct entry in admin_group_1 from physical and virtual combined
            for tag_group_1 in admin_cluster_grouping_1_rows :
                tag_group_1_str = "%1s" % tag_group_1
                current_cluster_group = "group_1_"+tag_group_1_str+" "
                # Add every ip address from the master server list
                for server in range(len(master_server_list_rows)) :                    
                    if tag_group_1_str in master_server_list_rows[server][1] :  
                        current_cluster_group += "%1s " % master_server_list_rows[server][0]
                    pass
                pass
                file_handle.write(current_cluster_group + "\n\n")
            pass
        
        # Write a entry for every distinct entry in admin_group_2 from physical and virtual combined
            for tag_group_2 in admin_cluster_grouping_2_rows :
                tag_group_2_str = "%1s" % tag_group_2
                current_cluster_group = "group_2_"+tag_group_2_str+" "
                 # Add every ip address from the master server list
                for server in range(len(master_server_list_rows)) :                    
                    if tag_group_2_str in master_server_list_rows[server][2] :  
                        current_cluster_group += "%1s " % master_server_list_rows[server][0]
                    pass
                pass
                file_handle.write(current_cluster_group + "\n\n")
            pass
        
        finally:
            file_handle.close()
        pass
    pass
    
    database_connection.close()
    
# use /etc/clusters to generate a menu and launch cssh
def show_menu() :
    
    # Build a list of menu items
    menu_list = []
    lines = open("/etc/clusters","r").readlines()

    # Build a map of all cluster groups
    for i in range(0, len(lines)):
        words = lines[i].split()       
        if len(words) > 0:        
            menu_list.append([words[0],"X"])
        pass
    pass

    # the menu loop
    while(1):
        
        # print out the map as a menu
        for i, j in enumerate(menu_list):
                print " ["+j[1]+"]", "%2s"%i, ") "+j[0]

        print "Please enter your selection (s show command) (l Launches) (q exits) -> "
        
        choice = raw_input()
        
        # leave the results of last iterations on the top
        os.system("clear")
        # exit
        if choice == "q" or choice == "Q":
                sys.exit(0)
        # launch
        elif choice == "l" or choice == "L":
            cmd = "cssh "
            for i, j in enumerate(menu_list):
                if "*" in j[1] :
                    cmd += "%1s " % j[0]
                pass
            pass
            os.system(cmd)
        # show what would be launched
        elif choice == "s" or choice == "S":
            cmd = "cssh "
            for i, j in enumerate(menu_list):
                if "*" in j[1] :
                    cmd += "%1s " % j[0]
                pass
            pass
            print "Will run command -> "+cmd
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
                print "Invalid entry please choose again. Press q to exit."
            pass                                    
        pass
               
                
if __name__ == '__main__':
    build_cluster()
    show_menu()