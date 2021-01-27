from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login/'),

path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

path('child_signUp/', auth_views.LogoutView.as_view(template_name='child_sighUp.html'), name='child_signUp'),

path("register/", views.register, name='register')

]