from django.http import HttpResponse
from django.shortcuts import render, redirect
from child_care.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def register_view(request, *args, **kwargs):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    user = RegisterForm()
    return render(request, "register.html", {'form':user})

def login_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = AuthenticationForm()        
    return render(request, 'login.html', {'form': form})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})          

def playtime_view(request, *args, **kwargs):
    return render(request, "playtime.html", {})                
       
   