DATABASE_CONNECTION = {
                      'HOST' : 'localhost',
                      'USER' : 'root',
                      'PASSWORD' : '',
                      'SCHEMA' : 'linux-admin-toolkit'
}

IMPORT_SPREADSHEET_NAME = 'server_inventory_import.xls'

PRIMARY_KEY_MAP = {
    'enclosure' : {
        'admin_gui_enclosure_machine_list' : {
            'enclosure_machine_name' : 1,
            'primary_ip_address' : 2,
            'location_code' : 3,
            'point_of_contact' : 4            
        },
    },
    'physical' : {
        'admin_gui_physical_machine_list' : {
            'physical_server_name' : 1,
            'primary_ip_address' : 2,
            'role' : 3,
            'purpose' : 4,
            'point_of_contact' : 5,            
        }        
    },
    'virtual' : {
        'admin_gui_virtual_machine_list' : {
            'virtual_server_name' : 1,
            'primary_ip_address' : 2,
            'role' : 3,
            'purpose' : 4,
            'point_of_contact' : 5                        
        }
    },
    'storage' : {
        'admin_gui_storage_machine_list' : {
            'storage_machine_name' : 1,
            'primary_ip_address' : 2,            
            'purpose' : 3,
            'point_of_contact' : 4,
            'location_code' : 5,
            'service_tag' : 6,
            'model' : 7,             
        }
    }    
}

SECONDARY_KEY_MAP = {
    'enclosure' : {
        'admin_gui_enclosure_machine_detail' : {
            'enclosure_machine_list_id' : 1,
            'service_tag' : 5,
            'model' : 6   
        },
    },
    'enclosures_additonal_ip' : {
        'admin_gui_enclosure_machine_additional_ip' : {
            'enclosure_machine_list_id' : 1,
            'additional_ip' : 2
        }
    },
    'enclosure_wire_run' : {
        'admin_gui_enclosure_machine_wire_run' : {
            'enclosure_machine_list_id' : 1,
            'source_port' : 2,
            'destination_machine_name' : 3,
            'destination_port' :  4
        }
    },
    'physical' : {        
        'admin_gui_physical_machine_detail' : {
            'physical_machine_list_id' : 1,
            'location_code' : 7,
            'service_tag' : 8,
            'console_address' : 9,
            'os' : 10,
            'model' : 11,
            'size' : 12                        
        },
        'admin_gui_physical_machine_services' : {
            'physical_machine_list_id' : 1,
            'admin_cluster_group_01' : 13,
            'admin_cluster_group_02' : 14,
            'script_profile' : 15                
        }           
    },
    'physical_additional_ip' : {
        'admin_gui_physical_machine_additional_ip' : {
            'physical_machine_list_id' : 1,
            'additional_ip' : 2
        }
    },
    'physical_wire_run' : {
        'admin_gui_physical_machine_wire_run' : {
            'physical_machine_list_id' : 1,
            'source_port' : 2,
            'destination_machine_name' : 3,
            'destination_port' :  4
        }
    },
    'virtual' : {        
        'admin_gui_virtual_machine_detail' : {
            'virtual_machine_list_id' : 1,
            'size' : 7,             
            'os' : 8,
            'base_image' : 9 
                                   
        },
        'admin_gui_virtual_machine_services' : {
            'virtual_machine_list_id' : 1,
            'admin_cluster_group_01' : 10,
            'admin_cluster_group_02' : 11,
            'script_profile' : 12                         
        }           
    },
    'storage_additional_ip' : {
        'admin_gui_storage_machine_additional_ip' : {
            'storage_machine_list_id' : 1,
            'additional_ip' : 2
        }
    },
    'storage_wire_run' : {
        'admin_gui_storage_machine_wire_run' : {
            'storage_machine_list_id' : 1,
            'source_port' : 2,
            'destination_machine_name' : 3,
            'destination_port' :  4
        }
    }
}

RELATIONSHIP_MAP = {
    'physical' : {
        'admin_gui_physical_machine_list' : {            
            'value_label' : 'host_enclosure_name_id',
            'value_column' : 6,
            'key_label' : 'physical_server_name',
            'key_column' : 1
        }
    },
    'virtual' : {
        'admin_gui_virtual_machine_list' : {            
            'value_label' : 'host_server_name_id',
            'value_column' : 6,
            'key_label' : 'virtual_server_name',
            'key_column' : 1
        }
    }
}