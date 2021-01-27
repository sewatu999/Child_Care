from django import forms
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request, *args, **kwargs):
    # if request.method == "GET":
    #     return render(request, template_name= 'register.html')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login')
    user = RegisterForm()
    return render(request, "register.html", {'form': user})

def login(request, *args, **kwargs):
    if request.method == "GET":
        return render('accounts/login/')
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()        
    return render(request, 'accounts/login.html', {'form': form})

def logout(request, *args, **kwargs):
    my_context = {
        "my_text": "Logged Out!"
    }
    return render(request, "accounts/logout.html", my_context)          
