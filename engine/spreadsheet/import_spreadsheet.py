#!/usr/bin/python
'''
Created on May 31, 2012

@author: David Davidson
'''
#modules part of default python library
import os
#modules installed by os (yum or apt-get)
import MySQLdb          #@UnresolvedImport
# Modules installed with EasyInstall 
import xlrd             #@UnresolvedImport
from configobj import ConfigObj #@UnresolvedImport


#config_path = os.path.abspath(__file__+"/../../../local-config/")
config_path = "/tmp/local-config/"

# load configuration data
config = ConfigObj(config_path+"/import_spreadsheet_config.dat")
dbconfig = ConfigObj(config_path+"/database_config.dat")

def main() :    
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(dbconfig['database_host'],dbconfig['database_user'], dbconfig['database_pass'], dbconfig['database_schema'])
    # open the spread sheet
    spread_sheet = config_path+config['spreadsheet_name']
    book = xlrd.open_workbook(spread_sheet)
    
    # iterate through every relevant spreadsheet sheet then iterate through every database table that is loaded from that sheet
    for sheet_to_load in config['import_map'] :
        print "Loading  worksheet "+sheet_to_load+" from "+config['spreadsheet_name']+"."
        
        worksheet = book.sheet_by_name(sheet_to_load)
        
        for database_table in config['import_map'][sheet_to_load] :
            print "Populating "+database_table+" in "+dbconfig['database_schema']
            
            # the 1 skips the header row
            for row_index in xrange(1,worksheet.nrows):
                cursor = db_connection.cursor ()
                
                # Create Query skeleton
                query_header = "INSERT INTO "+database_table
                query_column = " ("
                query_value = ") VALUES ("
                query_footer = ")"
                
                # Create each side of the map
                for map_index in config['import_map'][sheet_to_load][database_table] :
                    query_column += (map_index+", ")
                    col_index = int(config['import_map'][sheet_to_load][database_table][map_index])             
                    query_value += ("\""+worksheet.row_values(row_index)[col_index]+"\", ")
                pass
                
                
                #remove trailing commas
                query_column = query_column[:-2]
                query_value = query_value[:-2]
                # put the request in to the database
                try :
                    print "trying query -> "+query_header+query_column+query_value+query_footer
                    cursor.execute(query_header+query_column+query_value+query_footer)
                except Exception as e:
                    print e
            pass
        pass
    pass    # Python or no Python a good programmer closes their loops                
    
    # Write the actual data
    db_connection.commit()
    db_connection.close()
   
if __name__ == '__main__':
    main()
    