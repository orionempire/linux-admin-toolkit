IMPORT_SPREADSHEET_NAME = '/var/linux-admin-toolkit/server_inventory_import_export.xls'

PROJECT_TABLE_PREFIX= 'admin_gui_'

MODEL_TO_SPREADSHEET_MAP = {
    'enclosure' : [
        ['self','enclosure_name', 1],
        ['self','primary_ip_address',2],
        ['self','point_of_contact',3],
        ['self','status',4],
        ['self','location_code', 5],                    
        ['self','note', 8],
    ],
    'enclosure_detail' : [
        [['enclosure','enclosure_name'],'enclosure_id', 1],
        ['self','service_tag',6],
        ['self','model', 7 ]          
    ],
    'enclosure_additional_ip' : [       
        [['enclosure','enclosure_name'],'enclosure_id', 1],
        ['self','additional_ip',2],
    ],
    'enclosure_wire_run' : [
        [['enclosure','enclosure_name'],'enclosure_id', 1],
        ['self','source_port',2],
        ['self','destination_name',3],
        ['self','destination_port',4],            
    ],
    'physical' : [
        ['self','physical_name',1],
        ['self','primary_ip_address',2],
        ['self','role',3],
        ['self','purpose',4],
        ['self','point_of_contact',5],
        [['enclosure','enclosure_name'],'host_enclosure_name_id', 6],
        ['self','status',7],
        ['self','note',17],        
    ],       
    'physical_detail' : [
        [['physical','physical_name'],'physical_id', 1],
        ['self','location_code',8],
        ['self','service_tag',9],
        ['self','console_address',10],
        ['self','os',11],
        ['self','model',12],
        ['self','size',13],                 
    ],
    'physical_services' : [
        [['physical','physical_name'],'physical_id', 1],
        ['self','admin_cluster_group_01',14],
        ['self','admin_cluster_group_02',15],
        ['self','script_profile',16],
    ],
    'physical_additional_ip' : [
        [['physical','physical_name'],'physical_id', 1],
        ['self','additional_ip',2],            
    ],    
    'physical_wire_run' : [
        [['physical','physical_name'],'physical_id', 1],
        ['self','source_port',2],
        ['self','destination_name',3],
        ['self','destination_port',4],                        
    ],
    'virtual' : [
        ['self','virtual_name', 1],
        ['self','primary_ip_address',2],
        ['self','role',3],
        ['self','purpose',4],
        ['self','point_of_contact', 5],  
        [['physical','physical_name'],'host_physical_name_id', 6],                  
        ['self','status', 7],
        ['self','note', 14],            
    ],
    'virtual_detail' : [
        [['virtual','virtual_name'],'virtual_id', 1],
        ['self','size',2],
        ['self','os',3],
        ['self','base_image',4],           
    ],
    'virtual_services' : [
        [['virtual','virtual_name'],'virtual_id', 1],
        ['self','admin_cluster_group_01',11],
        ['self','admin_cluster_group_02',12],
        ['self','script_profile',13],                   
    ],
    'virtual_additional_ip' : [
        [['virtual','virtual_name'],'virtual_id', 1],
        ['self','additional_ip',2],            
    ], 
    'storage' : [
        ['self','storage_name',1],
        ['self','primary_ip_address',2],
        ['self','purpose',3],
        ['self','point_of_contact',4],
        ['self','status',5],
        ['self','location_code',6],
        ['self','service_tag',7],
        ['self','model',8],
        ['self','note',9],        
    ],       
    'storage_additional_ip' : [
        [['storage','storage_name'],'storage_id', 1],
        ['self','additional_ip',2],          
    ],
    'storage_wire_run' : [
        [['storage','storage_name'],'storage_id', 1],
        ['self','source_port',2],
        ['self','destination_name',3],
        ['self','destination_port',4],                        
    ],                                
}
