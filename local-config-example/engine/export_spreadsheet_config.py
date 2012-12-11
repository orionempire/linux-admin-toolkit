DATABASE_CONNECTION = {
                      'HOST' : 'localhost',
                      'USER' : 'root',
                      'PASSWORD' : '',
                      'SCHEMA' : 'linux-admin-toolkit'
}

EXPORT_SPREADSHEET_NAME = 'server_inventory_import_export.xls'

#Must be Null or Tuples! add comma to the end of single item tuples
EXPORT_MAP = {
     'enclosure' : {
        'field' : ('enclosure_name', 'primary_ip_address', 'point_of_contact', 'status', 'location_code', 'service_tag', 'model','note'),
        'table' : ('admin_gui_enclosure ','admin_gui_enclosure_detail'),
        'link'  : ('admin_gui_enclosure.enclosure_name=admin_gui_enclosure_detail.enclosure_id')
    },
    'enclosure_additional_ip' : {
        'field' : ('enclosure_id', 'additional_ip'),
        'table' : ('admin_gui_enclosure_additional_ip',),
        'link'  : ()
    },
    'enclosure_wire_run' : {
        'field' : ('enclosure_id', 'source_port', 'destination_name','destination_port'),
        'table' : ('admin_gui_enclosure_wire_run',),
        'link'  : ()
    },                       
    'physical' : {
        'field' : ('physical_name', 'primary_ip_address', 'role', 'purpose', 'point_of_contact', 'host_enclosure_name_id', 'status', 'location_code', 'service_tag', 'console_address', 'os', 'model', 'size', 'admin_cluster_group_01', 'admin_cluster_group_02', 'script_profile','note'),
        'table' : ('admin_gui_physical', 'admin_gui_physical_detail', 'admin_gui_physical_services'),        
        'link'  : 'admin_gui_physical.physical_name=admin_gui_physical_detail.physical_id and admin_gui_physical.physical_name=admin_gui_physical_services.physical_id'
    },                       
    'physical_additional_ip' : {
        'field' : ('physical_id','additional_ip'),
        'table' : (' admin_gui_physical_additional_ip',),
        'link'  : ()
    },         
    'physical_wire_run' : {
        'field' : ('physical_id', 'source_port', 'destination_name', 'destination_port'),
        'table' : ('admin_gui_physical_wire_run',),
        'link'  : ()
    },             
    'virtual' : {
        'field' : ('virtual_name', 'primary_ip_address', 'role', 'purpose', 'point_of_contact', 'host_physical_name_id',  'status', 'size', 'os', 'base_image', 'admin_cluster_group_01', 'admin_cluster_group_02', 'script_profile','note'),
        'table' : ('admin_gui_virtual','admin_gui_virtual_detail', 'admin_gui_virtual_services'),
        'link'  : ('admin_gui_virtual.virtual_name=admin_gui_virtual_detail.virtual_id and admin_gui_virtual.virtual_name=admin_gui_virtual_services.virtual_id')
    },
    'virtual_additional_ip' : {
        'field' : ('virtual_id','additional_ip'),
        'table' : ('admin_gui_virtual_additional_ip',),
        'link'  : ()
    }, 
    'storage' : {
        'field' : ('storage_name', 'primary_ip_address', 'purpose', 'point_of_contact', 'status', 'location_code', 'service_tag', 'model','note'),
        'table' : ('admin_gui_storage',),
        'link'  : ()
    }, 
    'storage_additional_ip' : {
        'field' : ('storage_id', 'additional_ip'),
        'table' : ('admin_gui_storage_additional_ip',),
        'link'  : ()
    },
    'storage_wire_run' : {
        'field' : ('storage_id', 'source_port', 'destination_name', 'destination_port'),
        'table' : ('admin_gui_storage_wire_run',),
        'link'  : ()
    }     
}
            

   