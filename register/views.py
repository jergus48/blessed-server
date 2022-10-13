# views.py
# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from main.models import Products

# Create your views here.
def register(response):
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid:
            form.save()
            
        return redirect("/")
    else:
        form=RegisterForm()
    return render(response, "register/register.html", {"form":form})
def redirect_login(request):
    if request.user.is_authenticated == False:
        response = redirect('/login/')
    else:
        response = redirect('/home/')
    return response




    
    
    
  