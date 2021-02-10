from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Register

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = "Child Care"

admin_site = MyAdminSite(name='myadmin') 
admin_site.register(Register)   

