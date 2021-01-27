from django.http import HttpResponse
from django.shortcuts import render, redirect
# from child_care.forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    my_context ={
        'text':  'Encouraging and moulding future leaders' 
    }
    
    return render(request, "home.html", my_context)

def about_owner(request):
    return render(request, "about_owner.html", {})          

def playtime(request):
    my_context = {
      "my_text": "A safe place for children to learn and play"  
    }
    return render(request, "playtime.html", my_context)                
       
   