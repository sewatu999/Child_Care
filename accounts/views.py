from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from .forms import RegisterForm
from .forms import ChildForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/child')
    else:        
        form = RegisterForm()
    return render(response, "register.html", {'form':form})

def login(request):
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

def child(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/playtime')
    else:   
        child = ChildForm()
    return render(response, "child.html", {'form': child})              
