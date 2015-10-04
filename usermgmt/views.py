from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from usermgmt.forms import Adduser, Usermod, Userdel, UserGrantAccess, UserForm, UserProfileForm
from django.contrib.auth.models import User
import  pwd
import crypt
import os
import sys
# Create your views here.

sys_sudo_pwd = 'halesh'

def home(request):
    """ """
    return render(request, 'usermgmt/home.html')

def index(request):
    adduser = Adduser()

    context_dict = {'add_user' : adduser}
    return render(request, 'usermgmt/index.html', context_dict)


def addsuccess(request):
    """ """
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
    """ """
    adduser = Usermod()

    context_dict = {'user_mod' : adduser}
    return render(request, 'usermgmt/usermod.html', context_dict)

def usermodsucc(request):
    """ """
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
    """ """
    userdel = Userdel()

    context_dict = {'user_del' : userdel}
    return render(request, 'usermgmt/userdel.html', context_dict)


def userdelsucc(request):
    """ """
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

def usergrant(request):
    """ """
    usergrant = UserGrantAccess()

    context_dict = {'user_grant' : usergrant}
    return render(request, 'usermgmt/usergrant.html', context_dict)

def usergrantsucc(request):
    """ """
    if request.method == 'POST':
 	username = request.POST.get('username')
	for user in pwd.getpwall():
	    if user[0] == username:
		username = username
	    	break
	user_grant = pwd.getpwnam('%s' %username) 
	if user[0] == username:
	    username = username

    return render(request, 'usermgmt/usergrantsucc.html', {'username': username})#, 'old_username': old_username})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user


            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'usermgmt/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

