
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,label="First Name and Last Name")
    last_name = forms.CharField(max_length=30, required=True,label="Instagram")
    
    username = forms.EmailField(max_length=254, required=True,label="Mail")
    first_name.widget.attrs.update( placeholder='First Name & Last Name')
    last_name.widget.attrs.update( placeholder='Instagram @')
    username.widget.attrs.update( placeholder='Unique Mail')
    password1= forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Password Confirmation")
    password1.widget.attrs.update( placeholder='Password')
    password2.widget.attrs.update( placeholder='Password Confirmation')
    email = forms.EmailField( required=False)



    class Meta:
        model = User
        fields = ["first_name","last_name", "username",'email', "password1", "password2"]






class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        error_messages = {
        'invalid_login': (
            "Please enter a correct mail and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': ("This account is inactive."),
    }
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={ 'placeholder': 'Your Mail'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={ 'placeholder':'Password'}) 
        self.fields['password'].label = False
        self.error_messages['invalid_login'] = "Please enter a correct mail and password."