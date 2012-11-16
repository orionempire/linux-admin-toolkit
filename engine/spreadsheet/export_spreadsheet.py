#!/usr/bin/python
'''
Created on Sept 19, 2012

@author: David Davidson
'''
import imp
#sudo pip install xlwt
import xlwt             #@UnresolvedImport

import MySQLdb          #@UnresolvedImport

config_path = "/home/sysadmin/workspace/linux-admin-toolkit/local-config-example/"
config_file = imp.load_source('*', config_path+'config_files/export_spreadsheet_config.py')

def do_export() :    
    do_flat_export(config_file.EXPORT_MAP) 
   
    
def do_flat_export(config_object) :    
    # connect to the database using values in the config file
    db_connection = MySQLdb.connect(config_file.DATABASE_CONNECTION['HOST'],config_file.DATABASE_CONNECTION['USER'], config_file.DATABASE_CONNECTION['PASSWORD'], config_file.DATABASE_CONNECTION['SCHEMA'])
    # open the spread sheet
    #spread_sheet = config_path+"data_files/"+config_file.EXPORT_SPREADSHEET_NAME
    book = xlwt.Workbook()
        
    #The sections must be cast to tuples     
    for sheet_to_export, query_section in config_object.items() :
        query = "SELECT "
        for field in query_section['field']:            
            query += field+", "
        query = query[:-2]
        query += " FROM "
        #for table in query_section['table'] :            
        for table in query_section['table'] :           
            query += table+", "
            
        query = query[:-2]
        
        if len(query_section['link']) > 0 :
            query += " WHERE "+query_section['link']
             
         
#        query += " WHERE "
#        for link in query_section['link']:
#            query += link+" = "
#        
#        if len(query_section['link']) == 0 : 
#            query = query[:-6]
#        else :
#            query = query[:-3]
        
        cursor = db_connection.cursor ()
    
        try :                        
            print "trying query -> "+query
            cursor.execute(query)        
        except Exception as e:
            print "ERROR ->",
            print e                    
        
        #Create spreedsheet tab
        current_sheet = book.add_sheet(sheet_to_export)
        
        font = xlwt.Font()
        font.bold = True
        font.underline = True
        style = xlwt.XFStyle()
        style.font = font
        
        
        #write the column titles on the first row
        i = 0
        for field in query_section['field'] :
            current_sheet.write(0, i, field,style)            
            i+=1
        
        #write the data
        i = 1         
        for row in cursor.fetchall() :
            j = 0
            for column in row :
                current_sheet.write(i, j, column) 
                j+=1
            i+=1
    pass
    
    book.save(config_path+"data_files/"+config_file.EXPORT_SPREADSHEET_NAME)

if __name__ == '__main__':
    do_export()