from django.conf.urls import patterns, include, url

from admin_gui.inventory_view import user_admin_site
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),        
    url(r'^view/', include(user_admin_site.urls)),    
    url(r'^','admin_gui.views.default')
)
