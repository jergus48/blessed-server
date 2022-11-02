# views.py
# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from main.models import Products

# Create your views here.
def register(response):
    display="none"
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            
            form.save()
            
            
        else:
            display="block"
            form=RegisterForm()
            
            return render(response, "register/register.html", {"form":form})
    else:
        form=RegisterForm()
    return render(response, "register/register.html", {"form":form,"display":display})
def redirect_login(request):
    if request.user.is_authenticated == False:
        response = redirect('/login/')
    else:
        response = redirect('/home/')
    return response




    
    
    
  