from django.http import HttpResponse

import os

def default(request):    
    return HttpResponse("Hello, world. You're at the base.")

def ping_sweep(request):
    if not request.user.is_staff:
        return Http404
    else : 
        path = os.path.join(os.path.dirname(__file__),'../../engine/network/ugly_ping_sweep.py')
        msg = "Run  "+path
        return HttpResponse(msg)
        
    