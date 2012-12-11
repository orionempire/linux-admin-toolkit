DATABASE_CONNECTION = {
                      'HOST' : 'localhost',
                      'USER' : 'root',
                      'PASSWORD' : '',
                      'SCHEMA' : 'linux-admin-toolkit'
}

IMPORT_SPREADSHEET_NAME = 'server_inventory_import_export.xls'

PRIMARY_KEY_MAP = {
    'enclosure' : {
        'admin_gui_enclosure' : {
            'enclosure_name' : 1,
            'primary_ip_address' : 2,
            'point_of_contact' : 3,
            'status' : 4,
            'location_code' : 5,                    
            'note' : 8,
        },
    },
    'physical' : {
        'admin_gui_physical' : {
            'physical_name' : 1,
            'primary_ip_address' : 2,
            'role' : 3,
            'purpose' : 4,
            'point_of_contact' : 5,
            'status' : 7, 
            'note' : 17,           
        }        
    },
    'virtual' : {
        'admin_gui_virtual' : {
            'virtual_name' : 1,
            'primary_ip_address' : 2,
            'role' : 3,
            'purpose' : 4,
            'point_of_contact' : 5,
            'status' : 7, 
            'note' : 14,                       
        }
    },
    'storage' : {
        'admin_gui_storage' : {
            'storage_name' : 1,
            'primary_ip_address' : 2,            
            'purpose' : 3,
            'point_of_contact' : 4,
            'status' : 5,  
            'location_code' : 6,
            'service_tag' : 7,
            'model' : 8,               
            'note' : 9,        
        }
    }    
}

SECONDARY_KEY_MAP = {
    'enclosure' : {
        'admin_gui_enclosure_detail' : {
            'enclosure_id' : 1,
            'service_tag' : 6,
            'model' : 7   
        },
    },
    'enclosure_additional_ip' : {
        'admin_gui_enclosure_additional_ip' : {
            'enclosure_id' : 1,
            'additional_ip' : 2
        }
    },
    'enclosure_wire_run' : {
        'admin_gui_enclosure_wire_run' : {
            'enclosure_id' : 1,
            'source_port' : 2,
            'destination_name' : 3,
            'destination_port' :  4
        }
    },
    'physical' : {        
        'admin_gui_physical_detail' : {
            'physical_id' : 1,
            'location_code' : 8,
            'service_tag' : 9,
            'console_address' : 10,
            'os' : 11,
            'model' : 12,
            'size' : 13                        
        },
        'admin_gui_physical_services' : {
            'physical_id' : 1,
            'admin_cluster_group_01' : 14,
            'admin_cluster_group_02' : 15,
            'script_profile' : 16,                
        }           
    },
    'physical_additional_ip' : {
        'admin_gui_physical_additional_ip' : {
            'physical_id' : 1,
            'additional_ip' : 2
        }
    },
    'physical_wire_run' : {
        'admin_gui_physical_wire_run' : {
            'physical_id' : 1,
            'source_port' : 2,
            'destination_name' : 3,
            'destination_port' :  4
        }
    },
    'virtual' : {        
        'admin_gui_virtual_detail' : {
            'virtual_id' : 1,
            'size' : 8,             
            'os' : 9,
            'base_image' : 10, 
                                   
        },
        'admin_gui_virtual_services' : {
            'virtual_id' : 1,
            'admin_cluster_group_01' : 11,
            'admin_cluster_group_02' : 12,
            'script_profile' : 13,                         
        }           
    },
    'virtual_additional_ip' : {
        'admin_gui_virtual_additional_ip' : {
            'virtual_id' : 1,
            'additional_ip' : 2
        }
    },
    'storage_additional_ip' : {
        'admin_gui_storage_additional_ip' : {
            'storage_id' : 1,
            'additional_ip' : 2
        }
    },
    'storage_wire_run' : {
        'admin_gui_storage_wire_run' : {
            'storage_id' : 1,
            'source_port' : 2,
            'destination_name' : 3,
            'destination_port' :  4
        }
    }
}

RELATIONSHIP_MAP = {
    'physical' : {
        'admin_gui_physical' : {            
            'value_label' : 'host_enclosure_name_id',
            'value_column' : 6,
            'key_label' : 'physical_name',
            'key_column' : 1
        }
    },
    'virtual' : {
        'admin_gui_virtual' : {            
            'value_label' : 'host_physical_name_id',
            'value_column' : 6,
            'key_label' : 'virtual_name',
            'key_column' : 1
        }
    }
}