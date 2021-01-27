from django.urls import path, reverse, NoReverseMatch
from child_care import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

    # path('register/', views.register, name='register')
    # path('login/', views.login, name='login')
    path('home/', views.home, name='home'),
    path('about_owner/', views.about_owner, name='about'),
    path('playtime/', views.playtime, name='playtime')
    # path('accounts/', include('accounts.urls'))
]