from django.contrib import admin
from .models import  Products,Wanted


class ProductsAdmin(admin.ModelAdmin):
    search_help_text="Product name"
    search_fields = ['name__icontains','name']
    list_display = ('name','size', 'user','image')
    list_filter = (
        ('user'),)
        
class WantedAdmin(admin.ModelAdmin):
    search_help_text="Wanted name"
    search_fields = ['name__icontains','name' ]
    list_display = ('name','size', 'user','image')
    list_filter = (
        ('user'),)
# Register your models here.
admin.site.register(Products,ProductsAdmin)
admin.site.register(Wanted,WantedAdmin)
# admin.site.register(Cart)
# admin.site.register(CartItem)

