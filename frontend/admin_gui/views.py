#sudo pip install django-tables2
from django.shortcuts import render, render_to_response
from admin_gui.models import *
from django.http import HttpResponse

def virtual_machine_list(request):
    return render(request, "virtual_machine_list.html", {"virtual_machine_list": Virtual_Machine_List.objects.all()})

def physical_machine_list(request):
    return render(request, "physical_machine_list.html", {"physical_machine_list": Physical_Machine_List.objects.all()})

def default(request):
    #return render("header.html")
    return render_to_response("base.html")