from django.urls import path
from . import views


urlpatterns = [

    path('register/', views.register, name='register')
    path('index/', views.index, name='index')
    path('login/', views.login, name='login')
    path('about/', views.about, name='about')
    path('playtime/', views.playtime, name='playtime')
]