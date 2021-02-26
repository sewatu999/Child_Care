from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import forms


def home(request):
    my_context ={
        'text':  'Encouraging and molding intelligent future leaders',
        # 'my_text': 'Phone Number: (937) 268-4395' 
    }
    
    return render(request, "home.html", my_context)

def staff(request):
    return render(request, "staff.html", {})          

def playtime(request):
    my_context = {
      "my_text": "A safe place for children to learn and play"  
    }
    return render(request, "playtime.html", my_context)

    
   