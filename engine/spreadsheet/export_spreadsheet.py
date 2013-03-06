#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp, sqlite3, os, glob, datetime

import xlrd             #@UnresolvedImport

config_file = imp.load_source('*', '../../local-config-files/import_spreadsheet_config.py')

def export_model(model_to_export, sheet_to_export):
    db_connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), '../../data/database.db'))  
    
    book = xlrd.open_workbook(config_file.IMPORT_SPREADSHEET_NAME)
    worksheet = book.sheet_by_name(sheet_to_export)        
   
    db_connection.close() 
def main():
    archive_globed_files(config_file.IMPORT_SPREADSHEET_NAME)
    export_model("enclosure","enclosure")
    
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