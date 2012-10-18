#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp
#sudo pip install xlrd
import xlrd             #@UnresolvedImport

import MySQLdb          #@UnresolvedImport


#config_path = "/etc/linux-admin-toolkit/"
config_path = "/home/sysadmin/workspace/linux-admin-toolkit/local-config-example/"
config_file = imp.load_source('*', config_path+'config_files/import_spreadsheet_config.py')

def do_import() :    
    do_import_primay_key_data()
    do_import_foriegn_key_data()

def do_import_foriegn_key_data() :
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    
    # open the spread sheet
    spread_sheet = config_path+"data_files/"+config_file.IMPORT_SPREADSHEET_NAME
    book = xlrd.open_workbook(spread_sheet)
    
    # iterate through every relevant spreadsheet sheet then iterate through every database table that is loaded from that sheet
    for sheet_to_load, data_maping in config_file.FORIEGN_KEY_MAP.items() :       
        print "Loading worksheet "+sheet_to_load+" from spreadsheet "+config_file.IMPORT_SPREADSHEET_NAME+"."    
        worksheet = book.sheet_by_name(sheet_to_load)
        
        # the 1 skips the header row
        for row_index in xrange(1,worksheet.nrows):
            cursor = db_connection.cursor ()
            select_query = "select "+data_maping['select_column_source']+" from "+data_maping['select_table']
            select_query += " where "+data_maping['select_column_condition']+" = \""+worksheet.row_values(row_index)[int(data_maping['select_sheet_column'] - 1)]+"\""
            update_query = "update "+data_maping['update_table']+" set "+data_maping['update_column']+" = ("+select_query+" ) "
            update_query += "where "+data_maping['update_column_condition']+" = \""+worksheet.row_values(row_index)[int(data_maping['update_sheet_column'] - 1)]+"\";"
            try :
                print "trying query -> "+update_query
                cursor.execute(update_query)
            except Exception as e:
                print e
            
    pass    # Python or no Python a good programmer closes their loops
            
    # Write the actual data
    db_connection.commit()
    db_connection.close()

def do_import_primay_key_data() : 
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    
    # open the spread sheet
    spread_sheet = config_path+"data_files/"+config_file.IMPORT_SPREADSHEET_NAME
    book = xlrd.open_workbook(spread_sheet)
    
    # iterate through every relevant spreadsheet sheet then iterate through every database table that is loaded from that sheet
    for sheet_to_load, database_table in config_file.PRIMARY_KEY_MAP.items() :       
        print "Loading worksheet "+sheet_to_load+" from spreadsheet "+config_file.IMPORT_SPREADSHEET_NAME+"."
        #print config_file.IMPORT_MAP[str(sheet_to_load)]
        worksheet = book.sheet_by_name(sheet_to_load)
                
        for database_table_name, data_maping in database_table.items() :
            print "Populating the "+database_table_name+" table in the "+config_file.DATABASE_CONNECTION['SCHEMA']+" database."
            
            # the 1 skips the header row
            for row_index in xrange(1,worksheet.nrows):
                cursor = db_connection.cursor ()
                # Create Query skeleton
                query_header = "INSERT INTO "+database_table_name
                query_column = " ("
                query_value = ") VALUES ("
                query_footer = ")"
                
                # Create each side of the map                                   
                for map_name, map_index in data_maping.items() :
                    query_column += (map_name+", ")
                    # Subtract 1 because the xlrd module indexes from zero
                    query_value += ("\""+worksheet.row_values(row_index)[int(map_index - 1)]+"\", ")                 
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
        pass    # Python or no Python a good programmer closes their loops
            
    # Write the actual data
    db_connection.commit()
    db_connection.close()
       
    
def main() :
    #TODO commandline allow import/export
    do_import()
        
   
if __name__ == '__main__':
    main()