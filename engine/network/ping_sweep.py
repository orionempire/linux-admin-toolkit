#! /usr/bin/python
'''
Created on 12/112012

@author: David Davidson

Assumption : 
'''
#modules part of default python library
import imp, os

#modules installed by os (yum or apt-get)
import MySQLdb          #@UnresolvedImport

config_path = "/etc/linux-admin-toolkit/"
config_file = imp.load_source('*', config_path+'engine/ping_sweep_config.py')

def main() :
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    
    for table, columns in config_file.PING_SWEEP_TABLES.items() :
        cursor = db_connection.cursor()
        
        print "Scanning table -> "+table
        cursor.execute("select "+columns[0]+","+columns[1]+" from "+table)
        working_list = cursor.fetchall()
        
        for item in working_list :
            if os.system("ping -c 1 -W 1 "+item[1]+">> /dev/null") :
                print item[1]+" is DEAD Executing ->"+"UPDATE "+table+" SET "+columns[2]+"=0 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
                cursor.execute("UPDATE "+table+" SET "+columns[2]+"=0 "+"WHERE "+columns[0]+"=\""+item[0]+"\"")
            else :
                print item[1]+" is Live Executing ->"+"UPDATE "+table+" SET "+columns[2]+"=1 "+"WHERE "+columns[0]+"=\""+item[0]+"\""
                cursor.execute("UPDATE "+table+" SET "+columns[2]+"=1 "+"WHERE "+columns[0]+"=\""+item[0]+"\"")                
        pass
    pass

    db_connection.commit()
    db_connection.close()
if __name__ == '__main__':
    main()