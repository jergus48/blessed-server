
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,label="First Name and Last Name")
    last_name = forms.CharField(max_length=30, required=True,label="Instagram")
    
    username = forms.EmailField(max_length=254, required=True,label="Mail")
    last_name.widget.attrs.update( placeholder='@')


    class Meta:
        model = User
        fields = ["first_name","last_name", "username", "password1", "password2"]
        