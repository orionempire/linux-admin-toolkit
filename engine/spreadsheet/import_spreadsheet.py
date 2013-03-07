#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp, sqlite3, os, sys

import xlrd             #@UnresolvedImport

config_file = imp.load_source('*', os.path.join(os.path.dirname(__file__), '../../local-config-files/import_export_spreadsheet_config.py'))


def import_model(model_to_import,sheet_to_import):
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))   
        
    book = xlrd.open_workbook(config_file.SPREADSHEET_TO_USE_NAME)
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
        for map_item in config_file.MODEL_TO_SPREADSHEET_MAP[model_to_import]:           
            if(map_item[0] == "self") :
                #if it is not a index item write the actual value                            
                query_value += ("\""+worksheet.row_values(row_index)[int(map_item[2] - 1)]+"\", ")
                query_column += (map_item[1]+", ")
            elif (map_item[0] == "default") :
                query_value += ("\""+map_item[2]+"\", ")
                query_column += (map_item[1]+", ")                                              
            elif (map_item[0] == "link") :
                # Write the actual value instead of the index number by using a sub query (ex enclosure_boo instead of 3)
                sub_query = "SELECT id FROM "+config_file.PROJECT_TABLE_PREFIX+map_item[1][0]+" WHERE "
                sub_query += map_item[1][1]+"=\""+worksheet.row_values(row_index)[int(map_item[2] - 1)]+"\""
                query_column += (map_item[1][2]+", ")
                print "....... trying sub query -> "+sub_query
                try :                        
                    sub_cursor.execute(sub_query)
                    value = str(sub_cursor.fetchone()[0])
                    query_value += ("\""+value+"\", ")
                except Exception as e:
                    query_value += ("null, ")
            else :
                print "ERROR -> Poorly formed map",
                sys.exit()                                    
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
    import_model("ancillary","ancillary")
    import_model("ancillary_additional_ip","ancillary_additional_ip")                
   
if __name__ == '__main__':
    main()