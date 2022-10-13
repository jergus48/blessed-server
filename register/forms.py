from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.EmailField(max_length=254, required=True,label="Mail")
    instagram=forms.CharField(max_length=30, required=True)


    class Meta:
        model = User
        fields = ["first_name","last_name", "username",'instagram', "password1", "password2"]
        