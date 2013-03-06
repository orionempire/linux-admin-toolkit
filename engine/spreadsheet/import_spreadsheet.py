#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp, sqlite3, os

import xlrd             #@UnresolvedImport

config_file = imp.load_source('*', '../../local-config-files/import_spreadsheet_config.py')

def import_model(model_to_import,sheet_to_import):
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))   
        
    book = xlrd.open_workbook(config_file.IMPORT_SPREADSHEET_NAME)
    worksheet = book.sheet_by_name(sheet_to_import)        
    
    for row_index in xrange(1,worksheet.nrows):
        cursor = db_connection.cursor ()
        sub_cursor = db_connection.cursor ()
        # Create Query skeleton
        query_header = "INSERT INTO "+config_file.PROJECT_TABLE_PREFIX+model_to_import
        query_column = " ("
        query_value = ") VALUES ("
        query_footer = ");"
        
        # Create each side of the map                                   
        for model_map in config_file.MODEL_TO_SPREADSHEET_MAP[model_to_import]:           
            if(model_map[0] == "self") :                            
                query_value += ("\""+worksheet.row_values(row_index)[int(model_map[2] - 1)]+"\", ")
            else :
                sub_query = "SELECT id FROM "+config_file.PROJECT_TABLE_PREFIX+model_map[0][0]+" WHERE "
                sub_query += model_map[0][1]+"=\""+worksheet.row_values(row_index)[int(model_map[2] - 1)]+"\""
                print "....... trying sub query -> "+sub_query
                try :                        
                    sub_cursor.execute(sub_query)
                    value = str(sub_cursor.fetchone()[0])
                    query_value += ("\""+value+"\", ")
                except Exception as e:
                    query_value += ("null, ")
                
                
            
            query_column += (model_map[1]+", ")                        
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
    
    db_connection.commit()
    db_connection.close()

def main():
    import_model("enclosure","enclosure")
    import_model("enclosure_detail","enclosure")
    import_model("enclosure_additional_ip","enclosure_additional_ip")
    import_model("enclosure_wire_run","enclosure_wire_run")
    import_model("physical","physical")
    import_model("physical_detail","physical")
    import_model("physical_services","physical")
    import_model("physical_additional_ip","physical_additional_ip")
    import_model("physical_wire_run","physical_wire_run")
    import_model("virtual","virtual")
    import_model("virtual_detail","virtual")
    import_model("virtual_services","virtual")
    import_model("virtual_additional_ip","virtual_additional_ip")    
    import_model("storage","storage")
    import_model("storage_additional_ip","storage_additional_ip")
    import_model("storage_wire_run","storage_wire_run")
    
        
   
if __name__ == '__main__':
    main()