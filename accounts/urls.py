from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .admin import admin_site
from . import views

urlpatterns = [
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login/'),

path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

path('register/', include("child_care.urls")),

path('login/', include("child_care.urls")),

path('child/', views.child, name='child'),

path('child/', include("child_care.urls")),

path("register/", views.register, name='register'),

path('myadmin/', admin_site.urls),

]