from django.http import HttpResponse

import os

def default(request):    
    return HttpResponse("Hello, world. You're at the base.")

def ping_sweep(request):    
    os.system("nohup ../engine/network/ugly_ping_sweep.py &")
    return HttpResponse("Kicked off a really sloppy ping sweep.")
    