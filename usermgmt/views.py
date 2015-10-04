from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usermgmt.forms import Adduser, Userdel
import  pwd
import crypt
import os
import sys
# Create your views here.

def index(request):
    adduser = Adduser()

    context_dict = {'add_user' : adduser}
    return render(request, 'usermgmt/index.html', context_dict)


def addsuccess(request):
    """"""
    if request.method == 'POST':
 	username = request.POST.get('username')
	password = request.POST.get('password')
	shelltype = request.POST.get('shelltype')
	userexist = None
	for user in pwd.getpwall():
	    if user[0] == username:
	    	userexist =  username
	    	break
	password = password
	encpass = crypt.crypt(password, '22')
	usercheck = os.system("echo  | sudo useradd "+username+" -p "+encpass+" -m -s /bin/bash")
	if user[0] == username:
	    userexist = username
	    print "User Doesn't exist in the server"
	    print "Creating the User: %s" %username
	else:
	   userexist = None
	   print "User already exist: %s" %username
        
	    
    return render(request, 'usermgmt/addsuccess.html', {'userexist': userexist, 'username': username})

def userdel(request):
    """"""
    userdel = Userdel()
    user_del = {'user_del': userdel}
    return render(request, 'usermgmt/userdel.html', user_del)
