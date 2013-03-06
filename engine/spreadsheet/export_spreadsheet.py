#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp, sqlite3, os, glob, datetime

import xlrd             #@UnresolvedImport

config_file = imp.load_source('*', '../../local-config-files/import_spreadsheet_config.py')

def export_model(sheet_to_export, models_to_use):
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))  
    
    #book = xlrd.open_workbook(config_file.IMPORT_SPREADSHEET_NAME)
    #worksheet = book.sheet_by_name(sheet_to_export)
    
    cursor = db_connection.cursor ()
    tmp1 = [0]*100
    tmp4 = []
    tmp5 = []
    
    for tmp2 in models_to_use :
        for tmp3 in config_file.MODEL_TO_SPREADSHEET_MAP[tmp2] :
            if tmp3[0] == "self" :                
                tmp1[tmp3[2]] = tmp3[1]
            else :
                if( tmp3[2] == 1) :
                    tmp5.append(config_file.PROJECT_TABLE_PREFIX+tmp2+"."+tmp3[1]+" = "+config_file.PROJECT_TABLE_PREFIX+tmp3[0][0]+".id")
                else :
                    #tmp1[tmp3[2]] = "(SELECT "+enclosure_name+" FROM "+admin_gui_enclosure+" WHERE id="+host_enclosure_name_id+") AS TEST"
                    tmp1[tmp3[2]] = "(SELECT "+tmp3[0][1]+" FROM "+config_file.PROJECT_TABLE_PREFIX+tmp3[0][0]+" WHERE id="+tmp3[1]+") AS "+tmp3[1]
        tmp4.append(tmp2)
    
    tmp1 = filter (lambda a: a != 0, tmp1)    
    
    query = "SELECT "
    for field in tmp1 :     
        query += field+", "
    #strip the last comma
    query = query[:-2]
    
    #Table
    query += " FROM "                    
    for table in tmp4 :           
        query += config_file.PROJECT_TABLE_PREFIX+table+", "
    #strip the last comma    
    query = query[:-2]
    
    #Where
    query += " WHERE "                    
    for table in tmp5 :           
        query += table+" AND "
    #strip the last AND    
    query = query[:-5]
    
    try :
        pass                        
        print "trying query -> "+query
        #cursor.execute(query)        
    except Exception as e:
        print "ERROR ->",
        print e       
    
    #tmp6 = cursor.fetchall()
    #print tmp6  
   
    #db_connection.close() 
def main():
    #archive_globed_files(config_file.IMPORT_SPREADSHEET_NAME,"n")
    export_model("enclosure",["enclosure","enclosure_detail"])
    export_model("physical",["physical","physical_detail","physical_services"])
    
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
            print "archiving -> ", file_name," to ->", new_location 
            os.system("mv "+file_name+" "+new_location)
        else:
            print "backing up -> ", file," to ->", new_location 
            os.system("cp "+file_name+" "+new_location)


if __name__ == '__main__':
    main()