from django.contrib import admin

from admin_gui.models import *
from django.forms.models import ModelForm

#by defualt django wont save tables that do not have  unique values.
#this messes up the export as the lookup querys fail. 
#By forcing a changed answer we ensure that the tables are written with their default value none. 
class AlwaysChangedModelForm(ModelForm):
    def has_changed(self):
        """ Should returns True if data differs from initial. 
        By always returning true even unchanged inlines will get validated and saved."""
        return True
    
# Admin view of all blade enclosures that can/will contain blades
class Enclosure_Additional_IP_Admin(admin.TabularInline):
    model = Enclosure_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1

class Enclosure_Wire_Run_Admin(admin.TabularInline):
    model = Enclosure_Wire_Run
    extra = 1
    
class Enclosure_Detail_Admin(admin.TabularInline):
    model = Enclosure_Detail
    form = AlwaysChangedModelForm
    
    
class Enclosure_Admin(admin.ModelAdmin):
    list_display = ['enclosure_name','primary_ip_address','location_code','point_of_contact','status','ip_active']    
    list_editable = ['status']
    list_filter=['location_code','point_of_contact','status']
    ordering = ['primary_ip_address']
    search_fields = ['enclosure_name','primary_ip_address','point_of_contact','location_code']
    readonly_fields = ['ip_active']
    inlines = [Enclosure_Detail_Admin, Enclosure_Additional_IP_Admin, Enclosure_Wire_Run_Admin]  
    actions = [make_active, make_inactive, make_maintenance]  
    
admin.site.register(Enclosure, Enclosure_Admin)

# Admin view of all physical servers and blades.
class Physical_Detail_Admin(admin.TabularInline):
    model = Physical_Detail
    readonly_fields = ['ip_active']
    form = AlwaysChangedModelForm
    
class Physical_Services_Admin(admin.TabularInline):
    model = Physical_Services
    extra = 1
    form = AlwaysChangedModelForm

class Physical_Additional_IP_Admin(admin.TabularInline):
    model = Physical_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1    

class Physical_Wire_Run_Admin(admin.TabularInline):
    model = Physical_Wire_Run
    extra = 1
            
class Physical_Admin(admin.ModelAdmin):
    list_display = ['physical_name','primary_ip_address','point_of_contact','role','purpose','host_enclosure_name','status','selected','ip_active']    
    list_editable = ['status','selected']
    list_filter=['role','purpose','host_enclosure_name','status']
    ordering = ['primary_ip_address']
    search_fields = ['physical_name','primary_ip_address','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Physical_Detail_Admin, Physical_Services_Admin, Physical_Additional_IP_Admin, Physical_Wire_Run_Admin]
    actions = [make_selected, make_unselected, make_active, make_inactive, make_maintenance]
    
admin.site.register(Physical, Physical_Admin )

# Admin view of virtual machines running the linux os.    
class Linux_Virtual_Detail_Admin(admin.TabularInline):
    model = Linux_Virtual_Detail
    extra = 1
    form = AlwaysChangedModelForm

class Linux_Virtual_Services_Admin(admin.TabularInline):
    model = Linux_Virtual_Services
    extra = 1
    form = AlwaysChangedModelForm
        
class Linux_Virtual_Additional_IP_Admin(admin.TabularInline):
    model = Linux_Virtual_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1
        
class Linux_Virtual_Admin(admin.ModelAdmin):
    list_display = ['linux_virtual_name','primary_ip_address','point_of_contact','role','purpose','host_physical_name','status','selected','ip_active']    
    list_editable = ['status','selected']
    list_filter=['role','purpose','host_physical_name','status']
    ordering = ['primary_ip_address']
    search_fields = ['linux_virtual_name','primary_ip_address','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Linux_Virtual_Detail_Admin, Linux_Virtual_Services_Admin, Linux_Virtual_Additional_IP_Admin]
    actions = [make_selected, make_unselected, make_active, make_inactive, make_maintenance]    
    
admin.site.register(Linux_Virtual, Linux_Virtual_Admin)

# Admin view of virtual machines running the a non-linux os.    
class Other_Virtual_Detail_Admin(admin.TabularInline):
    model = Other_Virtual_Detail
    extra = 1
    form = AlwaysChangedModelForm
        
class Other_Virtual_Additional_IP_Admin(admin.TabularInline):
    model = Other_Virtual_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1
        
class Other_Virtual_Admin(admin.ModelAdmin):
    list_display = ['other_virtual_name','primary_ip_address','point_of_contact','role','purpose','host_physical_name','status','ip_active']    
    list_editable = ['status']
    list_filter=['role','purpose','host_physical_name','status']
    ordering = ['primary_ip_address']
    search_fields = ['other_virtual_name','primary_ip_address','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Other_Virtual_Detail_Admin, Other_Virtual_Additional_IP_Admin]
    actions = [make_selected, make_unselected, make_active, make_inactive, make_maintenance]    
    
admin.site.register(Other_Virtual, Other_Virtual_Admin)
    
class Storage_Additional_IP_Admin(admin.TabularInline):
    model = Storage_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1

class Storage_Wire_Run_Admin(admin.TabularInline):
    model = Storage_Wire_Run
    extra = 1
            
class Storage_Admin(admin.ModelAdmin):
    list_display = ['storage_name','primary_ip_address','purpose','point_of_contact','location_code','service_tag','model','status','ip_active']    
    list_editable = ['status']
    list_filter=['purpose','location_code','model','status']
    ordering = ['primary_ip_address']
    search_fields = ['storage_name','primary_ip_address','point_of_contact','service_tag']
    readonly_fields = ['ip_active']
    inlines = [Storage_Additional_IP_Admin, Storage_Wire_Run_Admin]
    actions = [make_active, make_inactive, make_maintenance]
    
admin.site.register(Storage, Storage_Admin)

class Storage_Volume_Note_Admin(admin.TabularInline):
    model = Storage_Volume_Note
    extra = 1
    
class Storage_Volume_Admin(admin.ModelAdmin):
    list_display = ['volume_name','size','mount_point','role','purpose','host_storage_name','status']    
    list_display = ['volume_name','size','mount_point','role','purpose','status']
    list_editable = ['status']
    list_filter=['role','purpose','host_storage_name']
    ordering = ['volume_name']
    search_fields = ['volume_name','size','mount_point','role','purpose','host_storage_name']
    search_fields = ['volume_name','size','mount_point','role','purpose']    
    inlines = [Storage_Volume_Note_Admin]
    actions = [make_active, make_inactive, make_maintenance]
    
admin.site.register(Storage_Volume, Storage_Volume_Admin)
    
class Network_Additional_IP_Admin(admin.TabularInline):
    model = Network_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1

class Network_Wire_Run_Admin(admin.TabularInline):
    model = Network_Wire_Run
    extra = 1

class Network_Admin(admin.ModelAdmin):
    list_display = ['network_name','primary_ip_address','purpose','point_of_contact','location_code','service_tag','model','status','ip_active']    
    list_editable = ['status']
    list_filter=['purpose','location_code','model','status']
    ordering = ['primary_ip_address']
    search_fields = ['network_name','primary_ip_address','point_of_contact','service_tag']
    readonly_fields = ['ip_active']
    inlines = [Network_Additional_IP_Admin, Network_Wire_Run_Admin]
    actions = [make_active, make_inactive, make_maintenance]
    
admin.site.register(Network, Network_Admin)


