from django.db import models
from django.forms import ModelForm

# Create your models here.

class Register(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200)
    emergency_phonenumber = models.IntegerField(blank=True)

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ["firstname", "lastname", "username", "password", "email", "emergency_contact", ] 
        
class Child(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    parentsname = models.CharField(max_length=200)
    medications = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    

class ChildForm(ModelForm):    
    class Meta:
        model = Child
        fields = ["firstname", "lastname", "parentsname", "nickname", "medications", "date_of_birth", "age"] 
                