from django.contrib import admin

from admin_gui.models import *

# Admin view of all blade enclosures that can/will contain blades
class Enclosure_Machine_Additional_IP_Admin(admin.TabularInline):
    model = Enclosure_Machine_Additional_IP
    extra = 1

class Enclosure_Machine_Wire_Run_Admin(admin.TabularInline):
    model = Enclosure_Machine_Wire_Run
    extra = 1
    
class Enclosure_Machine_Detail_Admin(admin.TabularInline):
    model = Enclosure_Machine_Detail    
    
class Enclosure_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['enclosure_machine_name','primary_ip_address','location_code','point_of_contact']
    list_editable = ['primary_ip_address','location_code','point_of_contact']
    ordering = ['primary_ip_address']
    search_fields = ['enclosure_machine_name','point_of_contact']
    inlines = [Enclosure_Machine_Detail_Admin, Enclosure_Machine_Additional_IP_Admin, Enclosure_Machine_Wire_Run_Admin]    
    
admin.site.register(Enclosure_Machine_List,Enclosure_Machine_List_Admin)

# Admin view of all physical servers and blades.
class Physical_Machine_Detail_Admin(admin.TabularInline):
    model = Physical_Machine_Detail
    
class Physical_Machine_Services_Admin(admin.TabularInline):
    model = Physical_Machine_Services
    extra = 1

class Physical_Machine_Additional_IP_Admin(admin.TabularInline):
    model = Physical_Machine_Additional_IP
    extra = 1    

class Physical_Machine_Wire_Run_Admin(admin.TabularInline):
    model = Physical_Machine_Wire_Run
    extra = 1
            
class Physical_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['physical_server_name','primary_ip_address','point_of_contact','role','purpose','host_enclosure_name']
    list_filter=['host_enclosure_name','role','purpose']
    list_editable = ['primary_ip_address', 'point_of_contact', 'role', 'purpose', 'host_enclosure_name']
    ordering = ['primary_ip_address']
    search_fields = ['host_enclosure_name','point_of_contact']    
    inlines = [Physical_Machine_Detail_Admin, Physical_Machine_Services_Admin, Physical_Machine_Additional_IP_Admin, Physical_Machine_Wire_Run_Admin]
    
admin.site.register(Physical_Machine_List, Physical_Machine_List_Admin )

# Admin view of all physical servers and blades.    
class Virtual_Machine_Detail_Admin(admin.TabularInline):
    model = Virtual_Machine_Detail
    extra = 1

class Virtual_Machine_Services_Admin(admin.TabularInline):
    model = Virtual_Machine_Services
    extra = 1
        
class Virtual_Machine_Additional_IP_Admin(admin.TabularInline):
    model = Virtual_Machine_Additional_IP
    extra = 1
        
class Virtual_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['virtual_server_name','primary_ip_address','point_of_contact','role','purpose','host_server_name']
    list_filter=['host_server_name','role','purpose']
    list_editable = ['primary_ip_address','point_of_contact','role','purpose', 'host_server_name']
    ordering = ['primary_ip_address']
    search_fields = ['host_server_name','point_of_contact']
    inlines = [Virtual_Machine_Detail_Admin, Virtual_Machine_Services_Admin, Virtual_Machine_Additional_IP_Admin]    
    
admin.site.register(Virtual_Machine_List, Virtual_Machine_List_Admin)

    
class Storage_Machine_Additional_IP_Admin(admin.TabularInline):
    model = Storage_Machine_Additional_IP
    extra = 1

class Storage_Machine_Wire_Run_Admin(admin.TabularInline):
    model = Storage_Machine_Wire_Run
    extra = 1
    
        
class Storage_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['storage_machine_name','primary_ip_address','purpose','point_of_contact','location_code','service_tag','model']    
    list_editable = ['primary_ip_address','purpose','point_of_contact','location_code']
    ordering = ['primary_ip_address']
    search_fields = ['storage_machine_name','point_of_contact']
    inlines = [Storage_Machine_Additional_IP_Admin, Storage_Machine_Wire_Run_Admin]
    
admin.site.register(Storage_Machine_List,Storage_Machine_List_Admin)
