from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from . import forms
# from child_care.forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    my_context ={
        'text':  'Encouraging and molding intelligent future leaders',
        'my_text': 'Phone Number: (937) 268-4395' 
    }
    
    return render(request, "home.html", my_context)

def about_owner(request):
    return render(request, "about_owner.html", {})          

def playtime(request):
    my_context = {
      "my_text": "A safe place for children to learn and play"  
    }
    return render(request, "playtime.html", my_context)

def contact(request):
    if request.method == "POST":
        if form.is_valid():    
            subject = form.cleaned.data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['abduljames@gmail.com']
            if cc_myself:
                recipients.append(sender) 

            send_mail(subject, message, sender, recipient),    
    my_context = {
       "mess": "Send staff a message with any of your questions and concerns" 
    }
    return render(request, "contact.html", my_context)

       
   