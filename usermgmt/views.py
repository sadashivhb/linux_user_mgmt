from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usermgmt.forms import Adduser, Usermod, Userdel
import  pwd
import crypt
import os
import sys
# Create your views here.

sys_sudo_pwd = 'halesh'

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
	usercheck = os.system("echo "+sys_sudo_pwd+"  | sudo useradd "+username+" -p "+encpass+" -m -s /bin/bash")
	if user[0] == username:
	    userexist = username
	    print "User Doesn't exist in the server"
	    print "Creating the User: %s" %username
	else:
	   userexist = None
	   print "User already exist: %s" %username
        
	    
    return render(request, 'usermgmt/addsuccess.html', {'userexist': userexist, 'username': username})

def usermod(request):
    adduser = Usermod()

    context_dict = {'user_mod' : adduser}
    return render(request, 'usermgmt/usermod.html', context_dict)

def usermodsucc(request):
    """"""
    if request.method == 'POST':
 	old_username = request.POST.get('old_username')
 	new_username = request.POST.get('new_username')
	for user in pwd.getpwall():
	    if user[0] == old_username:
		old_username = old_username    	
	    	break
	user_modify= os.system("echo "+sys_sudo_pwd+" | sudo usermod -l "+new_username+" "+old_username+"")
	if user[0] == old_username:
	    old_username = old_username
        else:
	   new_username = new_username

    return render(request, 'usermgmt/usermodsucc.html', {'new_username': new_username, 'old_username': old_username})


def userdel(request):
    userdel = Userdel()

    context_dict = {'user_del' : userdel}
    return render(request, 'usermgmt/userdel.html', context_dict)


def userdelsucc(request):
    """"""
    if request.method == 'POST':
 	username = request.POST.get('username')
	for user in pwd.getpwall():
	    if user[0] == username:
		username = username
	    	break
	user_delete = os.system("echo "+sys_sudo_pwd+" | sudo userdel -r "+username+"")
	if user[0] == username:
	    username = username

    return render(request, 'usermgmt/userdelsucc.html', {'username': username})#, 'old_username': old_username})
