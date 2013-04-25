from django.conf.urls import patterns, url

from admin_gui import views

urlpatterns = patterns('',
    url(r'^ping_start$', views.ping_sweep, name='ping_sweep'), 
    url(r'^display_ip_report$', views.display_ip_report, name='display_ip_report'),
    url(r'^export_spreadsheet', views.export_spreadsheet, name='export_spreadsheet')
)