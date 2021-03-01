from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(label = "Enter First Name",max_length = 100)
    lastname = forms.CharField(label = "Enter Last Name",max_length = 100)
    phone_number = PhoneNumberField()
    email = forms.EmailField(label = "Enter email address",max_length = 200)
    # username = forms.CharField(label = "Enter Username",max_length=100)
    # password = forms.CharField(label = "Enter password",max_length = 200)
    emergency_contact = forms.CharField(label = "Enter Emergency Contact",max_length = 200)
    emergency_phonenumber = PhoneNumberField()
    class Meta:
        model = User
        fields = ["firstname", "lastname", "phone_number", "email", "emergency_contact", "emergency_phonenumber" ] 
        # widgets = {
        #     "password": forms.PasswordInput,
        #     # "email": forms.email

        # }

class login(AuthenticationForm):
    username = forms.CharField(label = "Enter username",max_length = 200)
    password = forms.CharField(label = "Enter password",max_length = 200)

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"password": forms.PasswordInput}

class ChildForm(forms.Form):
    firstname = forms.CharField(label = "Enter First Name",max_length = 200)
    lastname = forms.CharField(label = "Enter Last Name",max_length = 200)
    parentsname = forms.CharField(label="Enter Parents Full Name",max_length = 200)
    medications = forms.CharField(label = "Enter medications",max_length = 200)
    nickname = forms.CharField(label = "Enter nickname",max_length = 200, required = False)
    date_of_birth = forms.DateField(label = "Date of Birth")
    age = forms.IntegerField()
    
    
    class Meta:
        model = User
        fields = ["firstname", "lastname", "parentsname", "nickname", "medications", "date_of_birth", "age"] 
        
