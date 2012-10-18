DATABASE_CONNECTION = {
                      'HOST' : 'localhost',
                      'USER' : 'root',
                      'PASSWORD' : '',
                      'SCHEMA' : 'linux-admin-toolkit'
}

IMPORT_SPREADSHEET_NAME = 'server_inventory_import.xls'

PRIMARY_KEY_MAP = {
    'enclosures' : {
        'admin_gui_physical_enclosure_list' : {
            'enclosure_name' : 1,
            'primary_ip_address' : 2,
            'location_code' : 3,
            'point_of_contact' : 4,
            'service_tag' : 5,
            'model' : 6
        }
    },
    'linux_physical' : {
        'admin_gui_physical_machine_list' : {
            'server_name' : 1,
            'primary_ip_address' : 2,
            'role' : 3,
            'purpose' : 4,
            'point_of_contact' : 5,            
        }
    },
    'linux_virtual' : {
        'admin_gui_virtual_machine_list' : {
            'server_name' : 1,
            'primary_ip_address' : 2,
            'role' : 3,
            'purpose' : 4,
            'point_of_contact' : 5,
            'size' : 7,
            'os' : 8,
            'base_image' : 9,            
        } 
    },
    'storage_infrastructure' : {
        'admin_gui_storage_device_list' : {
            'device_name' : 1,
            'primary_ip_address' : 2,            
            'purpose' : 3,
            'point_of_contact' : 4,
            'location_code' : 5,
            'service_tag' : 6,
            'model' : 7,             
        }
    }
    
}

FORIEGN_KEY_MAP = {    
    'linux_physical' : {              
        'select_table' : 'admin_gui_physical_enclosure_list',                          
        'select_column_source' : 'id',        
        'select_column_condition' : 'enclosure_name',
        'select_sheet_column' : 6,
        'update_table' : 'admin_gui_physical_machine_list',
        'update_column' : 'host_enclosure_name_id',
        'update_column_condition' : 'server_name',
        'update_sheet_column' : 1
    },
    'linux_virtual' : {
        'select_table' : 'admin_gui_physical_machine_list',
        'select_column_source' : 'id',        
        'select_column_condition' : 'server_name',
        'select_sheet_column' : 6,
        'update_table' : 'admin_gui_virtual_machine_list',
        'update_column' : 'host_server_name_id',
        'update_column_condition' : 'server_name',
        'update_sheet_column' : 1    
    }
}
