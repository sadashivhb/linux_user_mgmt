import usermgmt
from django import forms

class Adduser(forms.Form):
    """"""
    username = forms.CharField(max_length=123)
    password = forms.CharField(widget=forms.PasswordInput)


