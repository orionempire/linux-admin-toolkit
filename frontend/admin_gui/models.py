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
class Enclosure(models.Model):    
    enclosure_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)    
    location_code = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    note = models.TextField(max_length=1024)    
    ip_active = models.BooleanField()    
    def __unicode__(self):
        return self.enclosure_name

# Model representing any additional IPs used by a blade enclosure.    
class Enclosure_Detail(models.Model):  
    enclosure =  models.OneToOneField(Enclosure, to_field='enclosure_name')
    service_tag = models.CharField(max_length=255)
    model = models.CharField(max_length=255)    

#Model representing any additional IPs used by a storage device.    
class Enclosure_Additional_IP(models.Model):  
    enclosure = models.ForeignKey(Enclosure, to_field='enclosure_name')
    additional_ip = models.CharField(max_length=255)
    ip_active = models.BooleanField()
    
# Model representing wire running from device to switch    
class Enclosure_Wire_Run(models.Model):  
    enclosure = models.ForeignKey(Enclosure, to_field='enclosure_name')
    source_port = models.CharField(max_length=255)
    destination_name = models.CharField(max_length=255)
    destination_port = models.CharField(max_length=255)     

###### Physical Machines ######

# Model representing all servers and blades, both might host Virtual machines and blades
# might be in a enclosure in which case its location is its slot.
class Physical(models.Model):    
    physical_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)    
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)           
    host_enclosure_name = models.ForeignKey(Enclosure, to_field='enclosure_name', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)
    note = models.TextField(max_length=1024)
    selected = models.BooleanField() 
    ip_active = models.BooleanField()    
    
    def __unicode__(self):
        return self.physical_name
       
# A one to one extension of the physical machine list      
class Physical_Detail(models.Model):
    physical = models.OneToOneField(Physical, to_field='physical_name')    
    location_code = models.CharField(max_length=255)
    service_tag = models.CharField(max_length=255)
    console_address = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    console_ip_active = models.BooleanField()   

class Physical_Services(models.Model):
    physical = models.OneToOneField(Physical, to_field='physical_name')
    admin_cluster_group_01 = models.CharField(max_length=255)
    admin_cluster_group_02 = models.CharField(max_length=255)
    script_profile = models.CharField(max_length=255)
    
#Model representing any additional IPs used by a storage device.    
class Physical_Additional_IP(models.Model):  
    physical = models.ForeignKey(Physical, to_field='physical_name')
    additional_ip = models.CharField(max_length=255)
    ip_active = models.BooleanField()
    
# Model representing wire running from device to switch    
class Physical_Wire_Run(models.Model):  
    physical = models.ForeignKey(Physical, to_field='physical_name')
    source_port = models.CharField(max_length=255)
    destination_name = models.CharField(max_length=255)
    destination_port = models.CharField(max_length=255)     

###### Virtual Machines ######
 
# Model representing a list of virtual machines. Must be hosted on a physical machine  
class Virtual(models.Model):
    virtual_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)   
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)    
    host_physical_name = models.ForeignKey(Physical, to_field='physical_name', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)
    selected = models.BooleanField() 
    ip_active = models.BooleanField()
    note = models.TextField(max_length=1024)   
    def __unicode__(self):
        return self.virtual_name

# A one to one extension of the virtual machine list 
class Virtual_Detail(models.Model):
    virtual = models.OneToOneField(Virtual, to_field='virtual_name')
    size = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    base_image = models.CharField(max_length=255)    

class Virtual_Services(models.Model):
    virtual = models.OneToOneField(Virtual, to_field='virtual_name')
    admin_cluster_group_01 = models.CharField(max_length=255)
    admin_cluster_group_02 = models.CharField(max_length=255)
    script_profile = models.CharField(max_length=255)
 
# Model representing any additional IPs used by a storage device.    
class Virtual_Additional_IP(models.Model):  
    virtual = models.ForeignKey(Virtual, to_field='virtual_name')
    additional_ip = models.CharField(max_length=255)
    ip_active = models.BooleanField()  
   
###### Storage ######

 #Model representing a list of storage devices likes SANS,MDSs,etc
class Storage(models.Model):
    storage_name = models.CharField(primary_key=True, max_length=255, unique=True)
    primary_ip_address = models.CharField(max_length=255,unique=True)    
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    location_code = models.CharField(max_length=255)
    service_tag = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES)
    ip_active = models.BooleanField()
    note = models.TextField(max_length=1024)  
    def __unicode__(self):
        return self.storage_name 
    
# Model representing any additional IPs used by a storage device.    
class Storage_Additional_IP(models.Model):  
    storage = models.ForeignKey(Storage, to_field='storage_name')
    additional_ip = models.CharField(max_length=255)
    ip_active = models.BooleanField()

# Model representing wire running from device to switch    
class Storage_Wire_Run(models.Model):  
    storage = models.ForeignKey(Storage, to_field='storage_name')
    source_port = models.CharField(max_length=255)
    destination_name = models.CharField(max_length=255)
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