from django.http import HttpResponse
#version 00.00.10
import os

def default(request):    
    return HttpResponse("Hello, world. You're at the base.")

def ping_sweep(request):
    if not request.user.is_staff:
        return Http404
    else : 
        os.system("rm -fr /var/linux-admin-toolkit/ip_reconciliate.txt")
        cmd_to_run = os.path.join(os.path.dirname(__file__),'../../engine/network/ping_sweep.py')        
        os.system("echo \""+cmd_to_run+"\" | at now")
        return HttpResponse("Kicked ping sweep. ("+cmd_to_run+")")
        
def display_ip_report(request):
    fileName=open("/var/linux-admin-toolkit/ip_reconciliate.txt")         
    lines = [i for i in fileName.readlines()]    
    lines.insert(0, "Also found at /var/linux-admin-toolkit/ip_reconciliate.txt\n")
    if not request.user.is_staff:
        return Http404
    else :                                
        response = HttpResponse(lines, mimetype='text/txt')
        response['Content-Disposition'] = 'inline; filename="foo.txt"'        
        pass       
        return response
        
    
def export_spreadsheet(request):
    if not request.user.is_staff:
        return Http404
    else :
        cmd_to_run = os.path.join(os.path.dirname(__file__),'../../engine/spreadsheet/export_spreadsheet.py')
        os.system(cmd_to_run)
        return HttpResponse("Running -> "+cmd_to_run+". Exported Spreadsheet to /var/linux-admin-toolkit/server_inventory_import_export.xls")

        
    