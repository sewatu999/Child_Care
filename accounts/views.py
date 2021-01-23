from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def register(request, *args, **kwargs):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = RegisterForm()
    return render(request, "register.html", {'form':form})

def login_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = AuthenticationForm()        
    return render(request, 'login.html', {'form': form})

def logout(request, *args, **kwargs):
    cc_context = {
        'cc_text': 'Logged Out!'
    }
    return render(request, "logout.html", cc_context)          
