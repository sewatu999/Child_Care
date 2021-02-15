"""child_care_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from child_care import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about_owner/', views.about_owner, name='about'),
    path('about_owner/', include('child_care.urls')),
    path('playtime/', views.playtime, name='playtime'),
    path('playtime/', include('child_care.urls')),
    path('contact/', views.contact, name='contact'),
    path('contact/', include('child_care.urls'))
       
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

   

urlpatterns += staticfiles_urlpatterns()
