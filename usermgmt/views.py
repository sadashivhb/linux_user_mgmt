from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usermgmt.forms import Adduser

# Create your views here.

def index(request):
    adduser = Adduser()
    
    context_dict = {'add_user' : adduser}
    return render(request, 'usermgmt/index.html', context_dict)


def addsuccess(request):
    context_dict = {'boldmessage':"Welcome to Django addsciccess"}
    return render(request, 'usermgmt/addsuccess.html', context_dict)
