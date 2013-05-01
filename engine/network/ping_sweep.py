#! /usr/bin/python
'''
Created on 04/25/2013

Version 00.00.12

@author: David Davidson

Assumption : 
'''

import imp, os, logging, sqlite3, re, nmap

config_file = imp.load_source('*', os.path.join(os.path.dirname(__file__), '../../local-config-files/ping_sweep_config.py'))

recorded_ip_list= {}
recorded_subnet_list = {}
file_out = open(config_file.RECONCILIATE_REPORT_NAME,'w')

def main() :
    #set up logging
    logging.basicConfig(
        level=logging.INFO,
        filename=config_file.RECONCILIATE_LOG_NAME, 
        format='%(asctime)s %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p',
    )    
    logging.info("Starting ping sweep")
    print "Writing --> /var/linux-admin-toolkit/ip_reconciliate.txt"        
    #Call calculation functions
    build_known_ip_list() 
    build_pingable_ip_list()
    #Generate Reports
    update_all_ip_actives()
    print_formated_report()
    logging.info("Finished ping sweep")
    file_out.close()       
pass


def build_known_ip_list() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db')) 
    
    #Build a list of all values in the db that are marked as such in the config file
    for table, columns in config_file.PING_SWEEP_TABLES.items() :
        cursor = db_connection.cursor()        
        logging.info("Scanning table -> "+table)
        
        #If a sub table was specified then there will be extra entries in the config file
        if(len(columns) == 2) :
            #Config file entry represents a item holding the ip and hostname       
            query = "select "+columns[0]+", "+columns[1]+" from "+config_file.PROJECT_TABLE_PREFIX+table
            logging.debug("Executing query ->"+query)
            cursor.execute(query)
            working_list = cursor.fetchall()
            catagory = table
        else :
            #Config file entry represents a item holding the ip and but the hostname need a lookup
            query = "select "+columns[0]+"," +columns[1]+" from "+config_file.PROJECT_TABLE_PREFIX+columns[2]+" INNER JOIN "+config_file.PROJECT_TABLE_PREFIX
            query += table+" ON "+config_file.PROJECT_TABLE_PREFIX+columns[2]+".id="+config_file.PROJECT_TABLE_PREFIX+table+"."+columns[3]
            logging.debug("Executing query ->"+query)
            cursor.execute(query)
            working_list = cursor.fetchall()
            catagory = columns[2]
        pass
        
        subnet_pattern = re.compile("\d{1,3}.\d{1,3}.\d{1,3}")
        for item in working_list :
            if(item[0] in recorded_ip_list) :                
                logging.error("(NON-FATAL) IP Address "+item[0]+" is a duplicate")
                file_out.write("ERROR -> IP Address "+item[0]+"("+catagory+") duplicate of "+str(recorded_ip_list[item[0]][0])+"("+str(recorded_ip_list[item[0]][2])+")\n")
            else :
                recorded_ip_list[item[0]] = [item[1],'INACTIVE',catagory]
            pass
            the_subnet = subnet_pattern.search(item[0]).group()        
            if( the_subnet in recorded_subnet_list) :
                recorded_subnet_list[the_subnet] += 1
            else :
                recorded_subnet_list[the_subnet] = 1
            pass
        pass  
    pass        
    
    db_connection.close()
pass

def build_pingable_ip_list() :
    nm=nmap.PortScanner()    
    for item in sorted(recorded_subnet_list) :          
        #nm.scan(hosts='192.168.16.0/24', arguments='-sn')
        logging.info("Scanning "+item+".0/24")
        nm.scan(hosts=str(item+'.0/24'), arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:        
            if( status == "up" ) :
                if host in recorded_ip_list :
                    recorded_ip_list[host][1] = 'ACTIVE'
                else :
                    recorded_ip_list[host]  = ['MISSING','ACTIVE','NONE']
                pass
            pass
        pass
        #break
    pass
pass

def update_all_ip_actives() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db')) 
             
    for table, columns in config_file.PING_SWEEP_TABLES.items() :
        cursor = db_connection.cursor()
                
        query = "select "+columns[0]+" from "+config_file.PROJECT_TABLE_PREFIX+table
        logging.debug("Executing query ->"+query)
        cursor.execute(query)        
        working_list = cursor.fetchall()        
        
        for item in working_list :            
            if (recorded_ip_list[item[0]][1] == 'ACTIVE' ):
                update_query="UPDATE "+config_file.PROJECT_TABLE_PREFIX+table+" SET ip_active=1 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
            else :
                update_query="UPDATE "+config_file.PROJECT_TABLE_PREFIX+table+" SET ip_active=0 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
            pass
            logging.debug("Executing update query ->"+update_query)            
            cursor.execute(update_query)
        pass
    pass
    
    db_connection.commit()    
    db_connection.close()    
pass

def print_formated_report() :
    file_out.write('------------------------------------------------------------------------\n')
    file_out.write('{0:16}     {1:20} |{3:15}| |{2:10}|\n'.format("IP Address", "Device Name", "Pingable", "Catagory"))
    file_out.write('------------------------------------------------------------------------\n')
    for item in sorted(recorded_ip_list) :
        file_out.write('{0:16} ==> {1:20} |{3:15}| |{2:10}|\n'.format(item, recorded_ip_list[item][0],recorded_ip_list[item][1],recorded_ip_list[item][2]))        
        pass
    pass
    file_out.write('---------------------------------------------\n')
    file_out.write('{0:16} ==> {1:20}\n'.format("Subnet", "Used Ip Address"))
    file_out.write('---------------------------------------------\n')
    for item in sorted(recorded_subnet_list) :        
        file_out.write('{0:16} ==> {1:3}\n'.format(item+".X", recorded_subnet_list[item]))        
        pass
    pass 
pass
if __name__ == '__main__':
    main()
