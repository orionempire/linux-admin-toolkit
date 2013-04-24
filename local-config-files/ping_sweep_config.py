UGLY_PING_SWEEP_TABLES = {
    'admin_gui_enclosure' : ['enclosure_name','primary_ip_address','ip_active'],
    'admin_gui_enclosure_additional_ip' : ['enclosure_id', 'additional_ip', 'ip_active'],
    'admin_gui_physical' : ['physical_name','primary_ip_address','ip_active'],
    'admin_gui_physical_additional_ip' : ['physical_id', 'additional_ip', 'ip_active'],
    'admin_gui_physical_detail' : ['physical_id', 'console_address', 'console_ip_active'],
    'admin_gui_storage' : ['storage_name','primary_ip_address','ip_active'],
    'admin_gui_storage_additional_ip' : ['physical_id', 'additional_ip', 'ip_active'],
    'admin_gui_linux_virtual' : ['linux_virtual_name','primary_ip_address','ip_active'],
    'admin_gui_linux_virtual_additional_ip' : ['linux_virtual_id', 'additional_ip', 'ip_active'],
    'admin_gui_other_virtual' : ['other_virtual_name','primary_ip_address','ip_active'],
    'admin_gui_other_virtual_additional_ip' : ['other_virtual_id', 'additional_ip', 'ip_active'],
    'admin_gui_network' : ['network_name','primary_ip_address','ip_active'],
    'admin_gui_network_additional_ip' : ['network_id', 'additional_ip', 'ip_active'],        
}

PING_SWEEP_PRIMARY_TABLES = {
    'admin_gui_enclosure' : ['primary_ip_address','enclosure_name'],
    'admin_gui_physical' : ['primary_ip_address','physical_name'],
    'admin_gui_storage' : ['primary_ip_address','storage_name'],    
    'admin_gui_linux_virtual' : ['primary_ip_address','linux_virtual_name'],    
    'admin_gui_other_virtual' : ['primary_ip_address','other_virtual_name'],    
    'admin_gui_network' : ['primary_ip_address','network_name']                   
}

PING_SWEEP_LINKED_TABLES = {    
    'admin_gui_enclosure_additional_ip' : ['additional_ip','enclosure_name', 'admin_gui_enclosure', 'enclosure_id',],    
    'admin_gui_physical_additional_ip' : ['additional_ip', 'physical_name', 'admin_gui_physical','physical_id'],
    'admin_gui_physical_detail' : ['console_address', 'physical_name', 'admin_gui_physical','physical_id'],
    'admin_gui_storage_additional_ip' : ['additional_ip', 'storage_name', 'admin_gui_storage','storage_id'],
    'admin_gui_linux_virtual_additional_ip' : ['additional_ip', 'linux_virtual_name', 'admin_gui_linux_virtual','linux_virtual_id'],
    'admin_gui_other_virtual_additional_ip' : ['additional_ip', 'other_virtual_name', 'admin_gui_other_virtual','other_virtual_id'],
    'admin_gui_network_additional_ip' : ['additional_ip', 'network_name', 'admin_gui_network', 'network_id'],        
}