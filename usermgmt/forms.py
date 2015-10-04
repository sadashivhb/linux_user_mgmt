import usermgmt
from django import forms

class Adduser(forms.Form):
    """"""
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
    shelltype = forms.CharField(max_length=128)
    

class Userdel(forms.Form):
    """"""
    username = forms.CharField(max_length=128)
