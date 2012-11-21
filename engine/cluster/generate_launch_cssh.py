#! /usr/bin/python
'''
Created on Jun 14, 2012

@author: David Davidson

Assumption : 
'''
#modules part of default python library
import imp,os,sys
#modules installed by os (yum or apt-get)
import MySQLdb          #@UnresolvedImport

config_path = "/etc/linux-admin-toolkit/"
#config_path = "/home/sysadmin/workspace/linux-admin-toolkit/local-config-example/"
config_file = imp.load_source('*', config_path+'frontend/local_settings.py')

def do_generate() :
    credentials = config_file.DATABASES['default']
    # connect to the database using values in the config file
    #db_connection = MySQLdb.connect(config_file.DATABASES['default']['HOST'],config_file.DATABASES['default']['USER'], config_file.DATABASES['default']['PASSWORD'], config_file.DATABASES['default']['NAME'])
    db_connection = MySQLdb.connect(credentials['HOST'],credentials['USER'], credentials['PASSWORD'],credentials['NAME'])
    
    print("Accessing database....")
    
    with db_connection:
        
        cursor = db_connection.cursor()

        # Cache a list of physical and virtual servers from the database
        cursor.execute("SELECT primary_ip_address, admin_cluster_group_01, admin_cluster_group_02\
                        FROM `linux-admin-toolkit`.admin_gui_physical_machine_list \
                        JOIN `linux-admin-toolkit`.admin_gui_physical_machine_services \
                        ON physical_machine_list_id=physical_server_name")
        physical_machine_list = cursor.fetchall()  
        cursor.execute("SELECT primary_ip_address, admin_cluster_group_01, admin_cluster_group_02\
                        FROM `linux-admin-toolkit`.admin_gui_virtual_machine_list \
                        JOIN `linux-admin-toolkit`.admin_gui_virtual_machine_services \
                        ON virtual_machine_list_id=virtual_server_name")
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
        
        
#        print cluster_map.items()
        
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