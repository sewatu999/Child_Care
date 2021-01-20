from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# from django import phoneNumber


class RegisterForm(UserCreationForm):
    firstname = forms.CharField(label="Enter First Name",max_length=100)
    lastname = forms.CharField(label="Enter Last Name",max_length=100)
    username = forms.CharField(label="Enter Username",max_length=100)
    password = forms.CharField(label="Enter password",max_length=200)
    # phonenumber = PhoneNumberField(label="Enter phone number",)
    # email = forms.EmailField(label="Enter email address",max_length=200, blank=True, unique=True)
    emergency_contact = forms.CharField(label="Enter Emergency Contact",max_length=200)
    # emergency_phonenumber = PhoneNumberField(label="Enter Emergency Phone Number",)

    class Meta:
        model = User
        fields = ["firstname", "lastname", "username", "password", "email", "emergency_contact", ] 
        widgets = {
            "password": forms.PasswordInput,
            # "email": forms.email

        }

class login(AuthenticationForm):
    username = forms.CharField(label="Enter username",max_length=100)
    password = forms.CharField(label="Enter password",max_length=200)

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {"password": forms.PasswordInput}
