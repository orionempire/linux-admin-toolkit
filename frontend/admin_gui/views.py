from django.http import HttpResponse

import os

def default(request):    
    return HttpResponse("Hello, world. You're at the base.")
    