from django.urls import path, reverse, NoReverseMatch
# from child_care.admin import admin_site
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

    # path('myadmin/', admin_site.urls),
    # path('login/', views.login, name='login')
    path('home/', views.home, name='home'),
    path('about_owner/', views.about_owner, name='about'),
    path('playtime/', views.playtime, name='playtime')
    # path('accounts/', include('accounts.urls'))
]
# path('about_owner/home/', views.home, name='home'),
