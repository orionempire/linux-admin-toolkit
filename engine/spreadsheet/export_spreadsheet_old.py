#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp,glob, os, datetime, fileinput, sys
#sudo pip install xlwt
import xlwt             #@UnresolvedImport

import MySQLdb          #@UnresolvedImport

config_path = "/etc/linux-admin-toolkit/"
config_file = imp.load_source('*', config_path+'engine/export_spreadsheet_config.py')

def do_export() :    
    do_flat_export(config_file.EXPORT_MAP) 

def get_prefferd_column_width(num_characters):
    if num_characters < 15 : 
        return int(15 * 256)   
    else:
        return int((1+num_characters) * 256)
    
def do_flat_export(config_object) :    
    
    archive_globed_files(config_path+"data_files/"+config_file.EXPORT_SPREADSHEET_NAME,"n")
    
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    #create the spreadsheet object
    book = xlwt.Workbook()
    
    #The sections must be cast to tuples in export_spradsheet_config
    for sheet_to_export, query_section in sorted(config_object.items()) :
        #Iterate the export map.
        #Field 
        query = "SELECT "
        for field in query_section['field']:            
            query += field+", "
        #strip the last comma
        query = query[:-2]
        
        #Table
        query += " FROM "                    
        for table in query_section['table'] :           
            query += table+", "
        #strip the last comma    
        query = query[:-2]
        
        #If this refers a parent table build it.         
        if len(query_section['link']) > 0 :
            query += " WHERE "+query_section['link']
             
        
        cursor = db_connection.cursor ()
    
        try :                        
            print "trying query -> "+query
            cursor.execute(query)        
        except Exception as e:
            print "ERROR ->",
            print e                    
        
        #Build the spreadsheet
        #Create spreadsheet tab
        current_sheet = book.add_sheet(sheet_to_export)
        
        font = xlwt.Font()
        font.bold = True            
        #style = xlwt.XFStyle()
        style = xlwt.easyxf('pattern: pattern solid, fore-colour grey25')
        style.font = font
        style.borders.bottom = 1
        
        
        #write the column titles on the first row
        i = 0
        for field in query_section['field'] :            
            current_sheet.col(i).width = get_prefferd_column_width(field.__len__())
            current_sheet.write(0, i, field,style)            
            i+=1
        pass
        
        #write the data on the additional rows 
        i = 1         
        for row in cursor.fetchall() :
            j = 0
            for column in row :
                current_sheet.write(i, j, column) 
                j+=1
            pass
            i+=1
        pass
    pass
    
    book.save(config_path+"data_files/"+config_file.EXPORT_SPREADSHEET_NAME)

def archive_globed_files(glb, preserve):
    now = datetime.datetime.now()
    #create the archive destination if it does not yet exist.
    try:    
        os.makedirs("/etc/linux-admin-toolkit/archive/")
    #ignore exception thrown if directory exists
    except :        
        pass
        
    filelist=glob.glob(glb)
    for file_name in filelist:
        new_location = "/etc/linux-admin-toolkit/archive/"+now.strftime("%Y-%m-%d-%I%M%S%p")+"_"+os.path.basename(file_name)        
        if preserve == "n":
            print "archiving -> ", file_name," to ->", new_location 
            os.system("mv "+file_name+" "+new_location)
        else:
            print "backing up -> ", file," to ->", new_location 
            os.system("cp "+file_name+" "+new_location)


if __name__ == '__main__':
    do_export()