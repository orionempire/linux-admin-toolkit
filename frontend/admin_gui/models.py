from django.db import models
# Python code representation of what the database will look like

# Model representing a list of all blade enclosures that can/will contain blades
class Physical_Enclosure_List(models.Model):
    enclosure_name = models.CharField(max_length=255,unique=True)
    primary_ip = models.CharField(max_length=255,unique=True)    
    location_code = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    service_tag = models.CharField(max_length=255)
    device_model = models.CharField(max_length=255) 
    #def console_address_link(self):
    def __unicode__(self):
        return self.enclosure_name

# Model representing any additional IPs used by a blade enclosure.    
class Physical_Enclosure_Additional_IP(models.Model):  
    physical_enclosure_list = models.ForeignKey(Physical_Enclosure_List)
    additional_ip = models.CharField(max_length=255) 
    additional_hostname = models.CharField(max_length=255) 

# Model representing all servers and blades, both might host Virtual machines and blades
# might be in a enclosure in which case its location is its slot.
class Physical_Machine_List(models.Model):
    server_name = models.CharField(max_length=255,unique=True)
    primary_ip = models.CharField(max_length=255,unique=True)    
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    enclosure_name = models.ForeignKey(Physical_Enclosure_List)    
    def __unicode__(self):
        return self.server_name
       

# A one to one extension of the physical machine list        
class Physical_Machine_Details(models.Model):
    physical_machine_list = models.OneToOneField(Physical_Machine_List)
    service_tag = models.CharField(max_length=255)
    location_code = models.CharField(max_length=255)
    console_ip = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    size = models.CharField(max_length=255)    

# Model representing a list of tags that can be used for scripted admin actions
class Physical_Machine_Cluster_Tag(models.Model):
     physical_machine_list = models.ForeignKey(Physical_Machine_List)
     admin_cluster_group = models.CharField(max_length=255)
     
# Model representing any additional IPs used by a physical server or blade.    
class Physical_Machine_Additional_IP(models.Model):  
    physical_machine_list = models.ForeignKey(Physical_Machine_List)
    additional_ip = models.CharField(max_length=255) 
    additional_hostname = models.CharField(max_length=255) 
     
 
# Model representing a list of virtual machines. Must be hosted on a physical machine  
class Virtual_Machine_List(models.Model):
    server_name = models.CharField(max_length=255,unique=True)
    primary_ip = models.CharField(max_length=255,unique=True)   
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    host_server = models.ForeignKey(Physical_Machine_List)
    size = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    base_image = models.CharField(max_length=255)
    def __unicode__(self):
        return self.server_name

# Model representing a list of tags that can be used for scripted admin actions
class Virtual_Machine_Cluster_Tag(models.Model):
     physical_machine_list = models.ForeignKey(Virtual_Machine_List)
     admin_cluster_group = models.CharField(max_length=255)
     
# Model representing any additional IPs used by virtual machines.    
class Virtual_Machine_Additional_IP(models.Model):  
    physical_machine_list = models.ForeignKey(Virtual_Machine_List)
    additional_ip = models.CharField(max_length=255) 
    additional_hostname = models.CharField(max_length=255)
    
class Storage_Device_List(models.Model):
    device_name = models.CharField(max_length=255,unique=True)
    primary_ip = models.CharField(max_length=255,unique=True)    
    purpose = models.CharField(max_length=255)
    point_of_contact = models.CharField(max_length=255)
    location_code = models.CharField(max_length=255)
    service_tag = models.CharField(max_length=255)
    device_model = models.CharField(max_length=255)
    #def console_address_link(self):
    def __unicode__(self):
        return self.device_name
    
# Model representing any additional IPs used by a blade enclosure.    
class Storage_Device_Additional_IP(models.Model):  
    storage_device_list = models.ForeignKey(Storage_Device_List)
    additional_ip = models.CharField(max_length=255) 
    additional_hostname = models.CharField(max_length=255) 
