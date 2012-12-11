DATABASE_CONNECTION = {
                      'HOST' : 'localhost',
                      'USER' : 'root',
                      'PASSWORD' : '',
                      'SCHEMA' : 'linux-admin-toolkit'
}

PING_SWEEP_TABLES = {
    'admin_gui_enclosure' : ['enclosure_name','primary_ip_address','ip_active'],
    'admin_gui_enclosure_additional_ip' : ['enclosure_id', 'additional_ip', 'ip_active'],
    'admin_gui_physical' : ['physical_name','primary_ip_address','ip_active'],
    'admin_gui_physical_additional_ip' : ['physical_id', 'additional_ip', 'ip_active'],
    'admin_gui_physical_detail' : ['physical_id', 'console_address', 'console_ip_active'],
    'admin_gui_storage' : ['storage_name','primary_ip_address','ip_active'],
    'admin_gui_storage_additional_ip' : ['storage_id', 'additional_ip', 'ip_active'],
    'admin_gui_virtual' : ['virtual_name','primary_ip_address','ip_active'],
    'admin_gui_virtual_additional_ip' : ['virtual_id', 'additional_ip', 'ip_active'],
        
}