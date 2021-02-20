from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned.data['to_email']
            from_email = form.cleaned.data['from_email']
            subject = form.cleaned.data['subject']
            message = form.cleaned.data['message']
            try:
                send_email(to_email,from_email, subject, message, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.') 
            return redirect("success")
    return render(request, 'email.html', {'form':form}) 

def successView(request):
    return HttpResponse('Success!, Thank you for your message.')              
