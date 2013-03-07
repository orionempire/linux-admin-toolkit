from django.conf.urls import patterns, url

from admin_gui import views

urlpatterns = patterns('',
    url(r'^ping_start$', views.ping_sweep, name='ping_sweep'), 
    url(r'^ping_stop$', views.kill_ping_sweep, name='kill_ping_sweep'),
    url(r'^export_spreadsheet', views.export_spreadsheet, name='export_spreadsheet')
)