#! /usr/bin/python
'''
Created on Mar 7, 2013

@author: David Davidson

Assumption : 
'''

import sqlite3, os, sys

def do_generate() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))
    
    print("Accessing database....")
    
    with db_connection:
        
        cursor = db_connection.cursor()

        # Cache a list of physical and virtual servers from the database
        virtual_query = "SELECT primary_ip_address, admin_cluster_group_01, admin_cluster_group_02, selected "
        virtual_query += "FROM admin_gui_virtual JOIN admin_gui_virtual_services ON virtual_id=admin_gui_virtual.id"
        #print "Executing -> "+virtual_query
        cursor.execute(virtual_query)
        physical_machine_list = cursor.fetchall()  
        physical_query = "SELECT primary_ip_address, admin_cluster_group_01, admin_cluster_group_02, selected "
        physical_query += "FROM admin_gui_physical JOIN admin_gui_physical_services ON physical_id=admin_gui_physical.id"        
        #print "Executing -> "+physical_query
        cursor.execute(physical_query)
        virtual_machine_list = cursor.fetchall()
        
        cluster_map = dict()
        cluster_map['all_servers'] = []
        cluster_map['physical_servers'] = []
        cluster_map['virtual_servers'] = []
        
        # Build a list of of all of the used admin groups        
        for item in physical_machine_list : 
            cluster_map["admin_group_"+item[1]] = []
            cluster_map["admin_group_"+item[2]] = []            
        pass        
            
        for item in virtual_machine_list :                    
            cluster_map["admin_group_"+item[1]] = []
            cluster_map["admin_group_"+item[2]] = []            
        pass
    
        #
        for entity in physical_machine_list :
            cluster_map['all_servers'].append(entity[0])
            cluster_map['physical_servers'].append(entity[0])
            cluster_map["admin_group_"+entity[1]].append(entity[0])
            cluster_map["admin_group_"+entity[2]].append(entity[0])
                        
                    
        for entity in virtual_machine_list :
            cluster_map['all_servers'].append(entity[0])
            cluster_map['virtual_servers'].append(entity[0])
            cluster_map["admin_group_"+entity[1]].append(entity[0])
            cluster_map["admin_group_"+entity[2]].append(entity[0])
                        
        
        
        print cluster_map.items()
        
        print("Building Cluster file....")                
        try:
            # generate the cluster file
            file_handle = open("/etc/clusters","w")            
            for key, value in sorted(cluster_map.items()) :
                file_handle.write(key+" ")
                for entry in value :
                    file_handle.write(entry+" ")
                file_handle.write("\n\n")
                
        finally:
            file_handle.close()            
        pass
        
    pass
    
    db_connection.close()

## use /etc/clusters to generate a menu and launch cssh
def do_show_menu() :
    
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
                print e
                print "Invalid entry please choose again. Press q to exit."
            pass                                    
        pass   
def main() :
    do_generate()
    do_show_menu()
    
    
if __name__ == '__main__':
    main()