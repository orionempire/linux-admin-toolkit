#! /usr/bin/python
'''
Created on 12/112012

@author: David Davidson

Assumption : 
'''
#TODO  ugly need to fix later

# kill ->  kill $(ps aux | grep ugly_ping_sweep.py | grep python | awk '{ print $2 }')
#modules part of default python library
import imp, os, sqlite3

config_file = imp.load_source('*', os.path.join(os.path.dirname(__file__), '../../local-config-files/ping_sweep_config.py'))

def main() :
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db')) 
    
    for table, columns in config_file.UGLY_PING_SWEEP_TABLES.items() :
        cursor = db_connection.cursor()
        
        print "Scanning table -> "+table
        cursor.execute("select "+columns[1]+" from "+table)
        working_list = cursor.fetchall()        
        
        for item in working_list :
            print "Executing -> ping -c 1 -W 1 "+item[0]+">> /dev/null"
            if os.system("ping -c 1 -W 1 "+item[0]+">> /dev/null") :                
                print item[0]+" is DEAD Executing ->"+"UPDATE "+table+" SET "+columns[2]+"=0 "+"WHERE "+columns[1]+"=\""+item[0]+"\""                
                cursor.execute("UPDATE "+table+" SET "+columns[2]+"=0 "+"WHERE "+columns[1]+"=\""+item[0]+"\"")                                
            else :
                print item[0]+" is Live Executing ->"+"UPDATE "+table+" SET "+columns[2]+"=1 "+"WHERE "+columns[1]+"=\""+item[0]+"\""                
                cursor.execute("UPDATE "+table+" SET "+columns[2]+"=1 "+"WHERE "+columns[1]+"=\""+item[0]+"\"")
                pass
            db_connection.commit()
        pass        
    pass

    
    db_connection.close()
if __name__ == '__main__':
    main()