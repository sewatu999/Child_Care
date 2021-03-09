from django.urls import path, reverse
from django.conf.urls import url, include
from django.contrib import admin
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

    # path('my_admin/', admin_site.urls),
    path('home/', views.home, name='home'),
    path('staff/', views.staff, name='staff'),
    path('playtime/', views.playtime, name='playtime'),
    
]
