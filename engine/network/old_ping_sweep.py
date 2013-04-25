#! /usr/bin/python
'''
Created on 12/112012

@author: David Davidson

Assumption : 
'''

import imp, os, sqlite3, re, nmap

config_file = imp.load_source('*', os.path.join(os.path.dirname(__file__), '../../local-config-files/ping_sweep_config.py'))

recorded_ip_list= {}
recorded_subnet_list = {}

def main() :
    print "Starting....."
    build_known_ip_list()
    build_subnet_list() 
    build_pingable_ip_list()      
    update_all_ip_actives()
    print_formated_list()
    print "finished"
pass

def update_all_ip_actives() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db')) 
             
    for table, columns in config_file.PING_SWEEP_PRIMARY_TABLES.items() :
        cursor = db_connection.cursor()
        
        #print "Scanning table -> "+table
        query = "select "+columns[0]+" from "+table
        cursor.execute(query)        
        working_list = cursor.fetchall()        
        
        for item in working_list :            
            if (recorded_ip_list[item[0]][1] == 'ACTIVE' ):
                update_query="UPDATE "+table+" SET ip_active=1 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
            else :
                update_query="UPDATE "+table+" SET ip_active=0 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
            pass            
            cursor.execute(update_query)
        pass
    pass

    for table, columns in config_file.PING_SWEEP_LINKED_TABLES.items() :
        cursor = db_connection.cursor()
        
        #print "Scanning table -> "+table
        query = "select "+columns[0]+" from "+table
        cursor.execute(query)        
        working_list = cursor.fetchall()        
        
        for item in working_list :            
            if (recorded_ip_list[item[0]][1] == 'ACTIVE' ):
                update_query="UPDATE "+table+" SET ip_active=1 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
            else :
                update_query="UPDATE "+table+" SET ip_active=0 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
            pass
            cursor.execute(update_query)
        pass
    pass
    
    db_connection.commit()    
    db_connection.close()    
pass

def build_pingable_ip_list() :
    nm=nmap.PortScanner()    
    for item in sorted(recorded_subnet_list) :          
        nm.scan(hosts='192.168.16.0/24', arguments='-sn')
        #print "Scanning "+item+".0/24"
        #nm.scan(hosts=item+'.0/24', arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:        
            if( status == "up" ) :
                if host in recorded_ip_list :
                    recorded_ip_list[host] = [recorded_ip_list[host][0],'ACTIVE']
                else :
                    recorded_ip_list[host]  = ['MISSING','ACTIVE']
                pass
            pass
        pass
        break
    pass
pass

def build_subnet_list() :
    subnet_pattern = re.compile("\d{1,3}.\d{1,3}.\d{1,3}")
    for item in recorded_ip_list :
        the_subnet = subnet_pattern.search(item).group()        
        if( the_subnet in recorded_subnet_list) :
            recorded_subnet_list[the_subnet] += 1
        else :
            recorded_subnet_list[the_subnet] = 1
        pass
    pass
     
pass

def build_known_ip_list() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db')) 
    
    #Build a list of all ip addresses 
    for table, columns in config_file.PING_SWEEP_PRIMARY_TABLES.items() :
        cursor = db_connection.cursor()
        
        #print "Scanning table -> "+table
        
        query = "select "+columns[0]+","+columns[1]+" from "+table
        cursor.execute(query)
        working_list = cursor.fetchall() 
        
        for item in working_list :
            if(item[0] in recorded_ip_list) :
                print "ERROR -> (NON-FATAL) IP Address "+item[0]+" Is a duplicate"
            else :
                recorded_ip_list[item[0]] = [item[1],'INACTIVE']
        pass
    pass    

    for table, columns in config_file.PING_SWEEP_LINKED_TABLES.items() :
        cursor = db_connection.cursor()
        
        #print "Scanning table -> "+table
        query = "select "+columns[0]+","+columns[1]+" from "+columns[2]+" INNER JOIN "+table+" ON "+columns[2]+".id="+table+"."+columns[3]        
        cursor.execute(query)
        working_list = cursor.fetchall() 
        
        for item in working_list :
            if(item[0] in recorded_ip_list) :                
                print "ERROR -> (NON-FATAL) IP Address "+item[0]+" Is a duplicate"
                pass
            else :
                recorded_ip_list[item[0]] = [item[1],'INACTIVE']
        pass
    pass
    
    db_connection.close()
pass

def print_formated_list() :
    print "Writing --> /var/linux-admin-toolkit/ip_reconciliate.txt"
    file_out = open('/var/linux-admin-toolkit/ip_reconciliate.txt','w')
    file_out.write('-------------------------------------------------------\n')
    file_out.write('{0:16}     {1:20}  |{2:10}|\n'.format("IP Address", "Device Name", "Pingable"))
    file_out.write('-------------------------------------------------------\n')
    for item in sorted(recorded_ip_list) :
        file_out.write('{0:16} ==> {1:20}  |{2:10}|\n'.format(item, recorded_ip_list[item][0],recorded_ip_list[item][1]))               
        pass
    pass
    file_out.write('---------------------------------------------\n')
    file_out.write('{0:16} ==> {1:20}\n'.format("Subnet", "Used Ip Address"))
    file_out.write('---------------------------------------------\n')
    for item in sorted(recorded_subnet_list) :        
        file_out.write('{0:16} ==> {1:3}\n'.format(item+".X", recorded_subnet_list[item]))        
        pass
    pass 
    file_out.close()   
pass

if __name__ == '__main__':
    main()