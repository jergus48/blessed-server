# views.py
# views.py
from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import RegisterForm
from main.models import Products
from django.core.mail import send_mail
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
def register(response):
    if response.user.is_authenticated == True:
        response=redirect('/home/')
        return response
    display="none"
    if response.method == "POST":
        doc=response.POST.copy()
        doc['email']=response.POST.get('username')
        print(doc)
        form=RegisterForm(doc)
        if form.is_valid():
            print("valid")
            
            
            form.save()
            email=response.POST.get('username')
            
            
            html_message = render_to_string('register/registrationmail.html', {'context': 'values'})
            plain_message = strip_tags(html_message)
            

            send_mail('Welcome to Blessed Store', plain_message, 'blessedstore.sk@gmail.com', [email], html_message=html_message)
            response = redirect('/')
            return response
            
            
        else:
            print("invalid")
            
            print(response.POST)
            
            display="block"
            form=RegisterForm()
            
           
    else:
        form=RegisterForm()
    return render(response, "register/register.html", {"form":form,"display":display})
# def redirect_login(request):
#     if request.user.is_authenticated == False:
#         response = redirect('/login/')
#     else:
#         response = redirect('/home/')
#     return response
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }


class MyLoginView(LoginView):
    
    authentication_form = MyAuthForm
    




    
    
    
  