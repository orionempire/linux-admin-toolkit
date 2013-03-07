from django.conf.urls import patterns, url

from admin_gui import views

urlpatterns = patterns('',
    url(r'^$', views.ping_sweep, name='ping_sweep')    
)