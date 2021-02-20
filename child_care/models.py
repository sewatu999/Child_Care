from django.db import models
from django.db.models import Model
# from django.contrib.auth.models import User
from django.forms.widgets import Textarea
# from django.core.mail import send_mail
from django.contrib import admin


# Create your models here.

class Contact(models.Model):
    your_email = models.EmailField(max_length = 200)
    message = models.TextField() 
    sender = models.EmailField(max_length = 200)
    cc_myself = models.BooleanField(null=True) 
   
    # class Meta:
    #     # model = Contact
    #     widget = {
    #             "message": Textarea(attrs={'cols': 100, 'rows': 100})
    #         }
    #     fields = ['your_email', 'message', 'sender', 'cc_myself']
    
