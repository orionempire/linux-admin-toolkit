DATABASE_CONNECTION = {
                      'HOST' : 'localhost',
                      'USER' : 'root',
                      'PASSWORD' : '',
                      'SCHEMA' : 'linux-admin-toolkit'
}

EXPORT_SPREADSHEET_NAME = 'server_inventory_export.xls'

#Must be Null or Tuples! add comma to the end of single item tuples
EXPORT_MAP = {
     'enclosure' : {
        'field' : ('enclosure_machine_name', 'primary_ip_address', 'location_code', 'point_of_contact', 'service_tag', 'model'),
        'table' : ('admin_gui_enclosure_machine_list ','admin_gui_enclosure_machine_detail'),
        'link'  : ('admin_gui_enclosure_machine_list.enclosure_machine_name=admin_gui_enclosure_machine_detail.enclosure_machine_list_id')
    },
    'enclosure_additional_ip' : {
        'field' : ('enclosure_machine_list_id', 'additional_ip'),
        'table' : ('admin_gui_enclosure_machine_additional_ip',),
        'link'  : ()
    },
    'enclosure_machine_wire_run' : {
        'field' : ('enclosure_machine_list_id', 'source_port', 'destination_machine_name','destination_port'),
        'table' : ('admin_gui_enclosure_machine_wire_run',),
        'link'  : ()
    },                       
    'physical' : {
        'field' : ('physical_server_name', 'primary_ip_address', 'role', 'purpose', 'point_of_contact', 'host_enclosure_name_id', 'location_code', 'service_tag', 'console_address', 'os', 'model', 'size', 'admin_cluster_group_01', 'admin_cluster_group_02', 'script_profile'),
        'table' : ('admin_gui_physical_machine_list', 'admin_gui_physical_machine_detail', 'admin_gui_physical_machine_services'),        
        'link'  : 'admin_gui_physical_machine_list.physical_server_name=admin_gui_physical_machine_detail.physical_machine_list_id and admin_gui_physical_machine_list.physical_server_name=admin_gui_physical_machine_services.physical_machine_list_id'
    },                       
    'physical_additional_ip' : {
        'field' : ('physical_machine_list_id','additional_ip'),
        'table' : (' admin_gui_physical_machine_additional_ip',),
        'link'  : ()
    },         
    'physical_wire_run' : {
        'field' : ('physical_machine_list_id', 'source_port', 'destination_machine_name', 'destination_port'),
        'table' : ('admin_gui_physical_machine_wire_run',),
        'link'  : ()
    },             
    'virtual' : {
        'field' : ('virtual_server_name', 'primary_ip_address', 'role', 'purpose', 'point_of_contact', 'host_server_name_id', 'size', 'os', 'base_image', 'admin_cluster_group_01', 'admin_cluster_group_02', 'script_profile'),
        'table' : ('admin_gui_virtual_machine_list','admin_gui_virtual_machine_detail', 'admin_gui_virtual_machine_services'),
        'link'  : ('admin_gui_virtual_machine_list.virtual_server_name=admin_gui_virtual_machine_detail.virtual_machine_list_id and admin_gui_virtual_machine_list.virtual_server_name=admin_gui_virtual_machine_services.virtual_machine_list_id')
    },
    'virtual_additional_ip' : {
        'field' : ('virtual_machine_list_id','additional_ip'),
        'table' : ('admin_gui_virtual_machine_additional_ip',),
        'link'  : ()
    }, 
    'storage' : {
        'field' : ('storage_machine_name', 'primary_ip_address', 'purpose', 'point_of_contact', 'location_code', 'service_tag', 'model'),
        'table' : ('admin_gui_storage_machine_list',),
        'link'  : ()
    }, 
    'storage_additional_ip' : {
        'field' : ('storage_machine_list_id', 'additional_ip'),
        'table' : ('admin_gui_storage_machine_additional_ip',),
        'link'  : ()
    },
    'storage_wire_run' : {
        'field' : ('storage_machine_list_id', 'source_port', 'destination_machine_name', 'destination_port'),
        'table' : ('admin_gui_storage_machine_wire_run',),
        'link'  : ()
    }     
}
            

   