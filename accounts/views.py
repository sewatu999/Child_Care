from django import forms
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .forms import ChildForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request):
    # if request.method == "GET":
    #     return render(request, template_name= 'register.html')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login')
    user = RegisterForm()
    return render(request, "register.html", {'form': user})

def login(request):
    # if request.method == "GET":
    #     return render('accounts/login/')
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('accounts/child')
    else:
        form = AuthenticationForm()        
    return render(request, '/login.html', {'form': form})

def logout(request, *args, **kwargs):
    my_context = {
        "my_text": "Logged Out!"
    }
    return render(request, "/logout.html", my_context)

def child(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playtime')
    child = ChildForm()
    return render(request, "child.html", {'form': child})              
