from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'boldmessage':"Welcome to Django 1.7"}
    return render(request, 'usermgmt/index.html', context_dict)
