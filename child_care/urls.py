from django.urls import path, reverse
from django.conf.urls import url, include
from django.contrib import admin
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [

    # path('my_admin/', admin_site.urls),
    path('home/', views.home, name='home'),
    path('about_owner/', views.about_owner, name='about'),
    path('playtime/', views.playtime, name='playtime'),
    path('contact/', views.contact, name='contact'),
    # path('about_owner/', include('child_care.views.urls')),
    # path('accounts/', include('accounts.urls'))
]
