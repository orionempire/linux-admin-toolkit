from django.contrib import admin

from admin_gui.models import *

# Admin view of all blade enclosures that can/will contain blades
class Physical_Enclosure_Additional_IP_Admin(admin.TabularInline):
    model = Physical_Enclosure_Additional_IP
    extra = 1
    
class Physical_Enclosure_List_Admin(admin.ModelAdmin):
    list_display = ['enclosure_name','primary_ip','location_code','point_of_contact','service_tag','device_model']
    list_editable = ['primary_ip','location_code','point_of_contact','service_tag','device_model']
    ordering = ['primary_ip']
    search_fields = ['enclosure_name','point_of_contact']
    inlines = [Physical_Enclosure_Additional_IP_Admin]    
    
admin.site.register(Physical_Enclosure_List, Physical_Enclosure_List_Admin)

# Admin view of all physical servers and blades.
class Physical_Machine_Details_Admin(admin.TabularInline):
    model = Physical_Machine_Details
    
class Physical_Machine_Cluster_Tag_Admin(admin.TabularInline):
    model = Physical_Machine_Cluster_Tag
    extra = 1

class Physical_Machine_Additional_IP_Admin(admin.TabularInline):
    model = Physical_Machine_Additional_IP
    extra = 1
        
class Physical_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['server_name','primary_ip','point_of_contact','role','purpose','enclosure_name']
    list_filter=['enclosure_name','role','purpose']
    list_editable = ['primary_ip', 'point_of_contact', 'role', 'purpose', 'enclosure_name']
    ordering = ['primary_ip']
    search_fields = ['enclosure_name','point_of_contact']
    inlines = [Physical_Machine_Details_Admin, Physical_Machine_Additional_IP_Admin, Physical_Machine_Cluster_Tag_Admin]    
    
admin.site.register(Physical_Machine_List, Physical_Machine_List_Admin)

# Admin view of all physical servers and blades.    
class Virtual_Machine_Cluster_Tag_Admin(admin.TabularInline):
    model = Virtual_Machine_Cluster_Tag
    extra = 1

class Virtual_Machine_Additional_IP_Admin(admin.TabularInline):
    model = Virtual_Machine_Additional_IP
    extra = 1
        
class Virtual_Machine_List_Admin(admin.ModelAdmin):
    list_display = ['server_name','primary_ip','point_of_contact','role','purpose','host_server']
    list_filter=['host_server','role','purpose']
    list_editable = ['primary_ip','point_of_contact','role','purpose', 'host_server']
    ordering = ['primary_ip']
    search_fields = ['enclosure_name','point_of_contact']
    inlines = [Virtual_Machine_Additional_IP_Admin, Virtual_Machine_Cluster_Tag_Admin]    
    
admin.site.register(Virtual_Machine_List, Virtual_Machine_List_Admin)

    
class Storage_Device_Additional_IP_Admin(admin.TabularInline):
    model = Storage_Device_Additional_IP
    extra = 1
    
class Storage_Device_List_Admin(admin.ModelAdmin):
    list_display = ['device_name','primary_ip','purpose','point_of_contact','location_code','service_tag','device_model']    
    list_editable = ['primary_ip','purpose','point_of_contact','location_code']
    ordering = ['primary_ip']
    search_fields = ['device_name','point_of_contact']
    inlines = [Storage_Device_Additional_IP_Admin]
    
admin.site.register(Storage_Device_List, Storage_Device_List_Admin)
