from django.db import models
# Python code representation of what the database will look like

STATUS_CHOICES = (
    ('active','Active'),
    ('deploy','Deploying'),
    ('maintenance','Maintenance'),
    ('suspended','Suspended'),
    ('planning','Planning'),
)
###### Blade Enclosures ######

# Model representing a list of all blade enclosures that can/will contain blades
class Enclosure_Machine_List(models.Model):    
    enclosure_machine_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)    
    location_code = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)              
    def __unicode__(self):
        return self.enclosure_machine_name

# Model representing any additional IPs used by a blade enclosure.    
class Enclosure_Machine_Detail(models.Model):  
    enclosure_machine_list =  models.OneToOneField(Enclosure_Machine_List, to_field='enclosure_machine_name')
    service_tag = models.CharField(max_length=255)
    model = models.CharField(max_length=255)    

#Model representing any additional IPs used by a storage device.    
class Enclosure_Machine_Additional_IP(models.Model):  
    enclosure_machine_list = models.ForeignKey(Enclosure_Machine_List, to_field='enclosure_machine_name')
    additional_ip = models.CharField(max_length=255)
    
# Model representing wire running from device to switch    
class Enclosure_Machine_Wire_Run(models.Model):  
    enclosure_machine_list = models.ForeignKey(Enclosure_Machine_List, to_field='enclosure_machine_name')
    source_port = models.CharField(max_length=255)
    destination_machine_name = models.CharField(max_length=255)
    destination_port = models.CharField(max_length=255)     

###### Physical Machines ######

# Model representing all servers and blades, both might host Virtual machines and blades
# might be in a enclosure in which case its location is its slot.
class Physical_Machine_List(models.Model):    
    physical_server_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)    
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)       
    host_enclosure_name = models.ForeignKey(Enclosure_Machine_List, to_field='enclosure_machine_name', null=True, blank=True, on_delete=models.SET_NULL)
    selected = models.BooleanField() 
    def __unicode__(self):
        return self.physical_server_name
       
# A one to one extension of the physical machine list      
class Physical_Machine_Detail(models.Model):
    physical_machine_list = models.OneToOneField(Physical_Machine_List, to_field='physical_server_name')    
    location_code = models.CharField(max_length=255)
    service_tag = models.CharField(max_length=255)
    console_address = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    size = models.CharField(max_length=255)   

class Physical_Machine_Services(models.Model):
    physical_machine_list = models.OneToOneField(Physical_Machine_List, to_field='physical_server_name')
    admin_cluster_group_01 = models.CharField(max_length=255)
    admin_cluster_group_02 = models.CharField(max_length=255)
    script_profile = models.CharField(max_length=255)
    
#Model representing any additional IPs used by a storage device.    
class Physical_Machine_Additional_IP(models.Model):  
    physical_machine_list = models.ForeignKey(Physical_Machine_List, to_field='physical_server_name')
    additional_ip = models.CharField(max_length=255)
    
# Model representing wire running from device to switch    
class Physical_Machine_Wire_Run(models.Model):  
    physical_machine_list = models.ForeignKey(Physical_Machine_List, to_field='physical_server_name')
    source_port = models.CharField(max_length=255)
    destination_machine_name = models.CharField(max_length=255)
    destination_port = models.CharField(max_length=255)     

###### Virtual Machines ######
 
# Model representing a list of virtual machines. Must be hosted on a physical machine  
class Virtual_Machine_List(models.Model):
    virtual_server_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)   
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)
    host_server_name = models.ForeignKey(Physical_Machine_List, to_field='physical_server_name', null=True, blank=True, on_delete=models.SET_NULL)
    selected = models.BooleanField()      
    def __unicode__(self):
        return self.virtual_server_name

# A one to one extension of the virtual machine list 
class Virtual_Machine_Detail(models.Model):
    virtual_machine_list = models.OneToOneField(Virtual_Machine_List, to_field='virtual_server_name')
    size = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    base_image = models.CharField(max_length=255)    

class Virtual_Machine_Services(models.Model):
    virtual_machine_list = models.OneToOneField(Virtual_Machine_List, to_field='virtual_server_name')
    admin_cluster_group_01 = models.CharField(max_length=255)
    admin_cluster_group_02 = models.CharField(max_length=255)
    script_profile = models.CharField(max_length=255)
 
# Model representing any additional IPs used by a storage device.    
class Virtual_Machine_Additional_IP(models.Model):  
    virtual_machine_list = models.ForeignKey(Virtual_Machine_List, to_field='virtual_server_name')
    additional_ip = models.CharField(max_length=255)    
   
###### Storage ######

 #Model representing a list of storage devices likes SANS,MDSs,etc
class Storage_Machine_List(models.Model):
    storage_machine_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)    
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    location_code = models.CharField(max_length=255)
    service_tag = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)   
    def __unicode__(self):
        return self.storage_machine_name 
    
# Model representing any additional IPs used by a storage device.    
class Storage_Machine_Additional_IP(models.Model):  
    storage_machine_list = models.ForeignKey(Storage_Machine_List, to_field='storage_machine_name')
    additional_ip = models.CharField(max_length=255)

# Model representing wire running from device to switch    
class Storage_Machine_Wire_Run(models.Model):  
    storage_machine_list = models.ForeignKey(Storage_Machine_List, to_field='storage_machine_name')
    source_port = models.CharField(max_length=255)
    destination_machine_name = models.CharField(max_length=255)
    destination_port = models.CharField(max_length=255)  


####################Setter Fuctions
def make_selected(modeladmin, request, queryset):
    queryset.update(selected=True)
    

def make_unselected(modeladmin, request, queryset):
    queryset.update(selected=False)
    
def make_active(modeladmin, request, queryset):
    queryset.update(status='active')

def make_inactive(modeladmin, request, queryset):
    queryset.update(status='suspended')
    
def make_maintenance(modeladmin, request, queryset):
    queryset.update(status='maintenance')