from django.contrib import admin
from .models import Cart, Products,Account,CartItem
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)

class AccountInline(admin.StackedInline):
    model=Account
    can_delete=False
    verbose_name_plural="Accounts"
class CustomizeduserAdmin(UserAdmin):
    inlines=(AccountInline,)
admin.site.unregister(User)
admin.site.register(User,CustomizeduserAdmin)