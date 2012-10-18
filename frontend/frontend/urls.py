from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),    
    url(r'^virtual_machine_list/','admin_gui.views.virtual_machine_list'),
    url(r'^physical_machine_list/','admin_gui.views.physical_machine_list'),
    url(r'^','admin_gui.views.default')
)
