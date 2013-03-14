from django.http import HttpResponse

#version 00.00.10
import os

def default(request):    
    return HttpResponse("Hello, world. You're at the base.")

def ping_sweep(request):
    if not request.user.is_staff:
        return Http404
    else : 
        cmd_to_run = os.path.join(os.path.dirname(__file__),'../../engine/network/ugly_ping_sweep.py >> /tmp/ping_sweep.log ')        
        os.system("echo \""+cmd_to_run+"\" | at now")
        return HttpResponse("Kicked off a ugly ping sweep. ("+cmd_to_run+")")
        
def kill_ping_sweep(request):
    if not request.user.is_staff:
        return Http404
    else :                 
        os.system(" kill $(ps aux | grep ugly_ping_sweep.py | grep python | awk '{ print $2 }')")
        return HttpResponse("Killed Ping sweep")
    
def export_spreadsheet(request):
    if not request.user.is_staff:
        return Http404
    else :
        cmd_to_run = os.path.join(os.path.dirname(__file__),'../../engine/spreadsheet/export_spreadsheet.py')
        os.system(cmd_to_run)
        return HttpResponse("Running -> "+cmd_to_run+". Exported Spreadsheet to /var/linux-admin-toolkit/server_inventory_import_export.xls")

        
    