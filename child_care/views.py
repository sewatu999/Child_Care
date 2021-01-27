from django.http import HttpResponse
from django.shortcuts import render, redirect
# from child_care.forms import RegisterForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    
    return render(request, "home.html")

# def register(request, *args, **kwargs):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     user = RegisterForm()
#     return render(request, "register.html", {'form':user})

# def login_view(request, *args, **kwargs):
#     if request.method == "POST":
#         form = AuthenticationForm(data= request.POST)
#         if form.is_valid():
#             return redirect('home')
#     else:
#         form = AuthenticationForm()        
#     return render(request, 'login.html', {'form': form})

# def logout(request, *args, **kwargs):
#     cc_context = {
#         'cc_text': 'Logged Out!'
#     }
#     return render(request, "logout.html", cc_context)          

def about(request):
    return render(request, "about.html", {})          

def playtime(request):
    my_context = {
      "my_text": "A safe place for children to learn and play"  
    }
    return render(request, "playtime.html", my_context)                
       
   