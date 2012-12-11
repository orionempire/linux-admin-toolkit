from django.contrib import admin

from admin_gui.models import *


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
    
class Enclosure_Admin(admin.ModelAdmin):
    list_display = ['enclosure_name','primary_ip_address','location_code','point_of_contact','status','ip_active']    
    list_editable = ['status']
    list_filter=['location_code','point_of_contact','status']
    ordering = ['primary_ip_address']
    search_fields = ['enclosure_name','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Enclosure_Detail_Admin, Enclosure_Additional_IP_Admin, Enclosure_Wire_Run_Admin]  
    actions = [make_active, make_inactive, make_maintenance]  
    
admin.site.register(Enclosure, Enclosure_Admin)

# Admin view of all physical servers and blades.
class Physical_Detail_Admin(admin.TabularInline):
    model = Physical_Detail    
    readonly_fields = ['console_ip_active']
    
class Physical_Services_Admin(admin.TabularInline):
    model = Physical_Services
    extra = 1

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
    list_filter=['host_enclosure_name','role','purpose','status']
    ordering = ['primary_ip_address']
    search_fields = ['host_enclosure_name','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Physical_Detail_Admin, Physical_Services_Admin, Physical_Additional_IP_Admin, Physical_Wire_Run_Admin]
    actions = [make_selected, make_unselected, make_active, make_inactive, make_maintenance]
    
admin.site.register(Physical, Physical_Admin )

# Admin view of all physical servers and blades.    
class Virtual_Detail_Admin(admin.TabularInline):
    model = Virtual_Detail
    extra = 1

class Virtual_Services_Admin(admin.TabularInline):
    model = Virtual_Services
    extra = 1
        
class Virtual_Additional_IP_Admin(admin.TabularInline):
    model = Virtual_Additional_IP
    readonly_fields = ['ip_active']
    extra = 1
        
class Virtual_Admin(admin.ModelAdmin):
    list_display = ['virtual_name','primary_ip_address','point_of_contact','role','purpose','host_physical_name','status','selected','ip_active']    
    list_editable = ['status','selected']
    list_filter=['host_physical_name','role','purpose','status']
    ordering = ['primary_ip_address']
    search_fields = ['host_physical_name','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Virtual_Detail_Admin, Virtual_Services_Admin, Virtual_Additional_IP_Admin]
    actions = [make_selected, make_unselected, make_active, make_inactive, make_maintenance]    
    
admin.site.register(Virtual, Virtual_Admin)

    
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
    list_filter=['point_of_contact','location_code','status']
    ordering = ['primary_ip_address']
    search_fields = ['storage_name','point_of_contact']
    readonly_fields = ['ip_active']
    inlines = [Storage_Additional_IP_Admin, Storage_Wire_Run_Admin]
    actions = [make_active, make_inactive, make_maintenance]
    
admin.site.register(Storage, Storage_Admin)
