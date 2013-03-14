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
    enclosure_name = models.CharField(max_length=255, unique=True)    
    primary_ip_address = models.GenericIPAddressField(unique=True,blank=True,null=True)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='planning')    
    location_code = models.CharField(max_length=255,default="none")
    point_of_contact = models.CharField(max_length=255,default="none")
    note = models.TextField(max_length=1024,default="none")    
    ip_active = models.BooleanField(default=False) 
    def __unicode__(self):        
        return self.enclosure_name

# Model representing any additional IPs used by a blade enclosure.    
class Enclosure_Detail(models.Model):  
    enclosure =  models.OneToOneField(Enclosure)
    service_tag = models.CharField(max_length=255,blank=True)
    model = models.CharField(max_length=255,blank=True)    
    def __unicode__(self):        
       return unicode(self.enclosure)

#Model representing any additional IPs used by a storage device.    
class Enclosure_Additional_IP(models.Model):  
    enclosure = models.ForeignKey(Enclosure)
    additional_ip = models.GenericIPAddressField(unique=True)
    ip_active = models.BooleanField(default=False)
    def __unicode__(self):        
       return unicode(self.enclosure)
    
# Model representing wire running from device to switch    
class Enclosure_Wire_Run(models.Model):  
    enclosure = models.ForeignKey(Enclosure)
    source_port = models.CharField(max_length=255,blank=True)
    destination_name = models.CharField(max_length=255,blank=True)
    destination_port = models.CharField(max_length=255,blank=True)
    def __unicode__(self):        
       return unicode(self.enclosure)

###### Physical Machines ######

# Model representing all servers and blades, both might host Virtual machines and blades
# might be in a enclosure in which case its location is its slot.
class Physical(models.Model):    
    physical_name = models.CharField(max_length=255, unique=True)
    primary_ip_address = models.GenericIPAddressField(unique=True,blank=True,null=True)    
    role = models.CharField(max_length=255,default="none")
    purpose = models.CharField(max_length=255,default="none")
    point_of_contact = models.CharField(max_length=255,default="none")           
    host_enclosure_name = models.ForeignKey(Enclosure, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='planning')
    note = models.TextField(max_length=1024,default="none")
    selected = models.BooleanField(default=False) 
    ip_active = models.BooleanField(default=False)            
    def __unicode__(self):        
       return self.physical_name
       
# A one to one extension of the physical machine list      
class Physical_Detail(models.Model):
    physical = models.OneToOneField(Physical)    
    location_code = models.CharField(max_length=255,blank=True)
    service_tag = models.CharField(max_length=255,blank=True)
    console_address = models.GenericIPAddressField(unique=True,blank=True,null=True)
    os = models.CharField(max_length=255,blank=True)
    model = models.CharField(max_length=255,blank=True)
    size = models.CharField(max_length=255,blank=True)
    console_ip_active = models.BooleanField(default=False)
    def __unicode__(self):        
       return unicode(self.physical)

class Physical_Services(models.Model):
    physical = models.OneToOneField(Physical)
    admin_cluster_group_01 = models.CharField(max_length=255,blank=True)
    admin_cluster_group_02 = models.CharField(max_length=255,blank=True)
    script_profile = models.CharField(max_length=255,blank=True)
    def __unicode__(self):        
       return unicode(self.physical)
    
#Model representing any additional IPs used by a storage device.    
class Physical_Additional_IP(models.Model):  
    physical = models.ForeignKey(Physical)
    additional_ip = models.GenericIPAddressField(unique=True)
    ip_active = models.BooleanField(default=False)
    def __unicode__(self):        
       return unicode(self.physical)
    
# Model representing wire running from device to switch    
class Physical_Wire_Run(models.Model):  
    physical = models.ForeignKey(Physical)
    source_port = models.CharField(max_length=255,blank=True)
    destination_name = models.CharField(max_length=255,blank=True)
    destination_port = models.CharField(max_length=255,blank=True)
    def __unicode__(self):        
       return unicode(self.physical)

###### Virtual Machines ######
 
# Model representing a list of virtual machines. Must be hosted on a physical machine  
class Virtual(models.Model):
    virtual_name = models.CharField( max_length=255, unique=True)
    primary_ip_address = models.GenericIPAddressField(unique=True,blank=True,null=True)   
    role = models.CharField(max_length=255,default="none")
    purpose = models.CharField(max_length=255,default="none")
    point_of_contact = models.CharField(max_length=255,default="none")    
    host_physical_name = models.ForeignKey(Physical, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='planning')
    selected = models.BooleanField(default=False)
    ip_active = models.BooleanField(default=False)
    note = models.TextField(max_length=1024,default="none")       
    def __unicode__(self):        
        return self.virtual_name

# A one to one extension of the virtual machine list 
class Virtual_Detail(models.Model):
    virtual = models.OneToOneField(Virtual)
    size = models.CharField(max_length=255,blank=True)
    os = models.CharField(max_length=255,blank=True)
    base_image = models.CharField(max_length=255,blank=True)
    def __unicode__(self):        
        return self.virtual
    
class Virtual_Services(models.Model):
    virtual = models.OneToOneField(Virtual)
    admin_cluster_group_01 = models.CharField(max_length=255,blank=True)
    admin_cluster_group_02 = models.CharField(max_length=255,blank=True)
    script_profile = models.CharField(max_length=255,blank=True)
    def __unicode__(self):        
        return self.virtual
    
# Model representing any additional IPs used by a storage device.    
class Virtual_Additional_IP(models.Model):  
    virtual = models.ForeignKey(Virtual)
    additional_ip = models.GenericIPAddressField(unique=True)
    ip_active = models.BooleanField(default=False)
    def __unicode__(self):        
        return self.virtual
    
###### Storage ######

 #Model representing a list of storage devices likes SANS,MDSs,etc
class Storage(models.Model):
    storage_name = models.CharField(max_length=255, unique=True)
    primary_ip_address = models.GenericIPAddressField(unique=True,blank=True,null=True)    
    purpose = models.CharField(max_length=255,default="none")
    point_of_contact = models.CharField(max_length=255,default="none")
    location_code = models.CharField(max_length=255,default="none")
    service_tag = models.CharField(max_length=255,default="none")
    model = models.CharField(max_length=255,default="none")
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='planning')
    ip_active = models.BooleanField(default=False)
    note = models.TextField(max_length=1024,default="none")  
    def __unicode__(self):        
        return self.storage_name
    
# Model representing any additional IPs used by a storage device.    
class Storage_Additional_IP(models.Model):  
    storage = models.ForeignKey(Storage)
    additional_ip = models.GenericIPAddressField(unique=True)
    ip_active = models.BooleanField(default=False)
    def __unicode__(self):        
        return self.storage

# Model representing wire running from device to switch    
class Storage_Wire_Run(models.Model):  
    storage = models.ForeignKey(Storage)
    source_port = models.CharField(max_length=255,blank=True)
    destination_name = models.CharField(max_length=255,blank=True)
    destination_port = models.CharField(max_length=255,blank=True)
    def __unicode__(self):        
        return self.storage

#Model representing Ancillary devices and virtual machines
class Auxilary(models.Model):
    auxilary_name =  models.CharField(max_length=255, unique=True)
    primary_ip_address = models.GenericIPAddressField(unique=True,blank=True,null=True)    
    purpose = models.CharField(max_length=255,default="none")
    point_of_contact = models.CharField(max_length=255,default="none")
    location_code = models.CharField(max_length=255,default="none")
    service_tag = models.CharField(max_length=255,default="none")
    model = models.CharField(max_length=255,default="none")
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,default='planning')
    ip_active = models.BooleanField(default=False)
    note = models.TextField(max_length=1024,default="none")  
    def __unicode__(self):        
        return self.ancillary_name

# Model representing any additional IPs used by a Ancillary device.    
class Auxilary_Additional_IP(models.Model):  
    auxilary = models.ForeignKey(Auxilary)
    additional_ip = models.GenericIPAddressField(unique=True)
    ip_active = models.BooleanField(default=False)
    def __unicode__(self):        
        return self.auxilary

####################Setter Functions
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
   
    