#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp, sqlite3, os, glob, datetime, sys, logging

import xlwt             #@UnresolvedImport

config_file = imp.load_source('*', os.path.join(os.path.dirname(__file__), '../../local-config-files/import_export_spreadsheet_config.py'))
log_level = level=logging.INFO

def main():
    #set up logging
    logging.basicConfig(
        level=log_level,
        filename=config_file.IMPORT_EXPORT_LOG_NAME, 
        format='%(asctime)s %(message)s', 
        datefmt='%m/%d/%Y %I:%M:%S %p',
    )
    logging.info("=======================================Starting export==============================================\n\n")
    archive_globed_files(config_file.SPREADSHEET_TO_USE_NAME,"n")
    #create the spreadsheet object
    book = xlwt.Workbook()    
    export_model(book, "enclosure",["enclosure","enclosure_detail"])
    export_model(book, "enclosure_additional_ip",["enclosure_additional_ip"])
    export_model(book, "enclosure_wire_run",["enclosure_wire_run"])
    export_model(book, "physical",["physical","physical_detail","physical_services"])
    export_model(book, "physical_additional_ip",["physical_additional_ip"])
    export_model(book, "physical_wire_run",["physical_wire_run"])
    export_model(book, "storage",["storage"])
    export_model(book, "storage_additional_ip",["storage_additional_ip"])
    export_model(book, "storage_volume",["storage_volume"])
    export_model(book, "storage_volume_note",["storage_volume_note"])
    export_model(book, "storage_wire_run",["storage_wire_run"])
    export_model(book, "linux_virtual",["linux_virtual","linux_virtual_detail","linux_virtual_services"])
    export_model(book, "linux_virtual_additional_ip",["linux_virtual_additional_ip"])
    export_model(book, "other_virtual",["other_virtual","other_virtual_detail"])
    export_model(book, "other_virtual_additional_ip",["other_virtual_additional_ip"])
    export_model(book, "network",["network"])
    export_model(book, "network_additional_ip",["network_additional_ip"])
    export_model(book, "network_wire_run",["network_wire_run"])
    book.save(config_file.SPREADSHEET_TO_USE_NAME)
    logging.info("=======================================Ending export==============================================\n\n")
pass#def

def export_model(book, sheet_to_export, models_to_use):
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))          
    
    current_sheet = book.add_sheet(sheet_to_export)
    
    cursor = db_connection.cursor ()
    # Pre initialize the list so that values can be added to proper index
    spreadsheet_columns = [0]*1000
    used_model_list = []
    used_conditions = []
    
    logging.info("Exporting -> Spreadsheet ("+sheet_to_export+") using db tables->"+str(models_to_use))
        
    #Any model used is a from condition
    for model in models_to_use :
        used_model_list.append(model)
    pass#for
           
    for model in models_to_use :
        #Iterate the relationships specified in the config file
        for map_item in config_file.MODEL_TO_SPREADSHEET_MAP[model] :
            # self indicates the value in the db table
            if map_item[0] == "self" :                            
                spreadsheet_columns[map_item[2]] = map_item[1]
            # default indicates it is a unsaved value
            elif (map_item[0] == "default") :
                #no need to export default values
                pass
            # link indicates it is a value that must be looked up else where
            elif (map_item[0] == "link") :             
                if( map_item[1][0] in used_model_list) :                    
                    used_conditions.append(config_file.PROJECT_TABLE_PREFIX+model+"."+map_item[1][2]+" = "+config_file.PROJECT_TABLE_PREFIX+map_item[1][0]+".id")
                else :                                        
                    spreadsheet_columns[map_item[2]] = "(SELECT "+map_item[1][1]+" FROM "+config_file.PROJECT_TABLE_PREFIX+map_item[1][0]+" WHERE id="+map_item[1][2]+") AS "+map_item[1][2]
            else :
                logging.ERROR("FATAL ERROR -> Poorly formed map")
                sys.exit()
            pass#if
        pass#for
    pass#for
        
    #compact the list of headers to the used map items
    spreadsheet_columns = filter (lambda a: a != 0, spreadsheet_columns)    
    
    query = "SELECT "
    for field in spreadsheet_columns :     
        query += field+", "
    pass#for
    #strip the last comma
    query = query[:-2]
    
    #Table
    query += " FROM "                    
    for table in used_model_list :           
        query += config_file.PROJECT_TABLE_PREFIX+table+", "
    pass#for

    #strip the last comma    
    query = query[:-2]
    
    #Build the Where side if there is one
    if len(used_conditions) > 0 :
        query += " WHERE "        
        for table in used_conditions :           
            query += table+" AND "
        pass#for
        #strip the last AND    
        query = query[:-5]
    pass#if
    
    try :
        pass                        
        logging.info("trying query -> "+query)
        cursor.execute(query)        
    except Exception as e:
        logging.error("ERROR -> "+e)
    
    
    font = xlwt.Font()
    font.bold = True            
    #style = xlwt.XFStyle()
    style = xlwt.easyxf('pattern: pattern solid, fore-colour grey25')
    style.font = font
    style.borders.bottom = 1
            
    i = 0
    for header in cursor.description :
        current_sheet.col(i).width = get_prefferd_column_width(header[0].__len__())
        current_sheet.write(0, i, header[0],style)
        i += 1
    pass#for   
    
    #write the data on the additional rows 
    i = 1         
    for row in cursor.fetchall() :
        logging.debug("Writing row -> "+str(row))
        j = 0
        for column in row :            
            current_sheet.write(i, j, column) 
            j+=1
        pass
        i+=1
    pass
   
    db_connection.close() 
pass#def

    
def archive_globed_files(glb, preserve):
    now = datetime.datetime.now()
    #create the archive destination if it does not yet exist.
    try:    
        os.makedirs("/var/linux-admin-toolkit/archive/")
    #ignore exception thrown if directory exists
    except :        
        pass
        
    filelist=glob.glob(glb)
    for file_name in filelist:
        new_location = "/var/linux-admin-toolkit/archive/"+now.strftime("%Y-%m-%d-%I%M%S%p")+"_"+os.path.basename(file_name)        
        if preserve == "n":
            msg = "archiving -> ", file_name," to ->", new_location
            logging.info(msg) 
            os.system("mv "+file_name+" "+new_location)
        else:
            logging.info("backing up -> ", file," to ->", new_location) 
            os.system("cp "+file_name+" "+new_location)
        pass#if
    pass#for
pass#def

def get_prefferd_column_width(num_characters):
    if num_characters < 15 : 
        return int(15 * 256)   
    else:
        return int((1+num_characters) * 256)
    pass#if
pass#def

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        if(sys.argv[1] == "debug"):
            log_level = level=logging.DEBUG
        pass
    pass
    main()
pass#if

#############################---------Notes------------#########################
#SELECT enclosure_name,primary_ip_address , service_tag FROM admin_gui_enclosure LEFT JOIN admin_gui_enclosure_detail ON admin_gui_enclosure_detail.enclosure_id = admin_gui_enclosure.id
#SELECT enclosure_name, primary_ip_address, point_of_contact, status, location_code, service_tag, model, note FROM admin_gui_enclosure  LEFT JOIN admin_gui_enclosure_detail ON admin_gui_enclosure_detail.enclosure_id = admin_gui_enclosure.id
