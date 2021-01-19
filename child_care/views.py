from django.http import HttpResponse
from django.shortcuts import render
from child_care.forms import RegisterForm

# Create your views here.

def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def register_view(request, *args, **kwargs):
    user = RegisterForm()
    return render(request, "register.html", {'form':user})
   