"""blessed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.models import User
from register.forms import MyAuthForm
from main import sitemaps as s



sitemaps= {
     'Products':s.ProductsSitemap,
     'Wanted':s.WantedSitemap,
     'static':s.StaticViewsSitemap,
     'active':s.ActiveViewsSitemap
 }

urlpatterns = [
        
        
        path('BlessYouSpravca/', admin.site.urls),
        path('', v.redirect_login,name="login"),
        path("register/", v.register, name="register"),
        path("sitemap.xml/", sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

        path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset/reset_password.html',html_email_template_name='reset/password_reset_html_email.html'),name='reset_password'),
        path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_sent.html'),name='password_reset_done'),
        path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_form.html'),name='password_reset_confirm'),
        path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),name='password_reset_complete'),
        path('', include("main.urls")),
        path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=MyAuthForm), name='login'),
        path('', include("django.contrib.auth.urls")),
        
    ]
handler404 = 'main.views.handler404'
# handler500 = 'main.views.handler500'

