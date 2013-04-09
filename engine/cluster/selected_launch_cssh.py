#! /usr/bin/python
'''
Created on Mar 7, 2013

@author: David Davidson

Assumption : 
'''
# Version 00.00.10

import sqlite3, os

def do_generate() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))
    
    print("Accessing database....")
    
    cursor = db_connection.cursor()

    # Cache a list of physical and virtual servers from the database
    linux_virtual_query = "SELECT primary_ip_address, admin_cluster_group_01, admin_cluster_group_02, selected "
    linux_virtual_query += "FROM admin_gui_linux_virtual JOIN admin_gui_linux_virtual_services ON linux_virtual_id=admin_gui_linux_virtual.id"
    print "Executing -> "+linux_virtual_query
    cursor.execute(linux_virtual_query)
    physical_machine_list = cursor.fetchall()  
    physical_query = "SELECT primary_ip_address, admin_cluster_group_01, admin_cluster_group_02, selected "
    physical_query += "FROM admin_gui_physical JOIN admin_gui_physical_services ON physical_id=admin_gui_physical.id"        
    print "Executing -> "+physical_query
    cursor.execute(physical_query)
    linux_virtual_machine_list = cursor.fetchall()
    
    selected_map = []
    
    for entity in physical_machine_list :            
        if(entity[3] == True) :
            selected_map.append(entity[0])
        pass
    pass
            
    for entity in linux_virtual_machine_list :            
        if(entity[3] == True) :
            selected_map.append(entity[0])
        pass
    pass
    
    cmd = "cssh "
    for item in selected_map:
        cmd += item+" "
    print "executing ->"+cmd
    os.system(cmd)
pass

def main() :
    do_generate()
    
    
    
if __name__ == '__main__':
    main()