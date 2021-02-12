from django.contrib import admin
from .models import Model

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = "Child Care"

admin_site = MyAdminSite(name='myadmin') 
admin_site.register(Model)   