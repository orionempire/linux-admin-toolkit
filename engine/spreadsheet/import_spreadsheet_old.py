#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp
#sudo pip install xlrd
import xlrd             #@UnresolvedImport

import MySQLdb          #@UnresolvedImport

config_path = "/etc/linux-admin-toolkit/"
config_file = imp.load_source('*', config_path+'engine/import_spreadsheet_config.py')

def do_import() :    
    do_import_key_data(config_file.PRIMARY_KEY_MAP)    
    do_import_key_data(config_file.SECONDARY_KEY_MAP)
    do_import_relationship_map(config_file.RELATIONSHIP_MAP)   
    
     
    
def do_import_relationship_map(config_object) :
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    
    # open the spread sheet
    spread_sheet = config_path+"data_files/"+config_file.IMPORT_SPREADSHEET_NAME
    book = xlrd.open_workbook(spread_sheet)
    
    # iterate through every relevant spreadsheet sheet then iterate through every database table that is loaded from that sheet       
    for sheet_to_load, database_table in config_object.items() :
        print "Loading worksheet "+sheet_to_load+" from spreadsheet "+config_file.IMPORT_SPREADSHEET_NAME+"."        
        worksheet = book.sheet_by_name(sheet_to_load)
                
        for database_table_name, data_mapping in database_table.items() :
            print "Creating the relationships in the "+database_table_name+" table of the "+config_file.DATABASE_CONNECTION['SCHEMA']+" database."
                       
            # the 1 skips the header row
            for row_index in xrange(1,worksheet.nrows):
                cursor = db_connection.cursor ()
                
                update_query = "UPDATE "+database_table_name+ " SET "+data_mapping['value_label']+"=\"" 
                update_query += worksheet.row_values(row_index)[int(data_mapping['value_column'] - 1)]+"\" WHERE "+data_mapping['key_label']+"=\""
                update_query += worksheet.row_values(row_index)[int(data_mapping['key_column'] -1)]+"\"" 
                try :                        
                    print "trying query -> "+update_query
                    cursor.execute(update_query)
                except Exception as e:
                    print "ERROR ->",
                    print e
            pass
        pass
    pass

    # Write the actual data
    db_connection.commit()
    db_connection.close()
    
def do_import_key_data(config_object) :
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    
    # open the spread sheet
    spread_sheet = config_path+"data_files/"+config_file.IMPORT_SPREADSHEET_NAME
    book = xlrd.open_workbook(spread_sheet)
    
    # iterate through every relevant spreadsheet sheet then iterate through every database table that is loaded from that sheet       
    for sheet_to_load, database_table in config_object.items() :
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
                query_footer = ");"
                
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
                    print "ERROR ->",
                    print e
            pass
        pass    # Python or no Python a good programmer closes their loops
            
    # Write the actual data
    db_connection.commit()
    db_connection.close()       
    
def main() :
    #TODO command line allow import/export
    do_import()
        
   
if __name__ == '__main__':
    main()