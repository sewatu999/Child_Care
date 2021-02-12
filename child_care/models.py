from django.db import models
from django.forms import ModelForm

# Create your models here.
class Contact(models.Model):
    your_email = models.EmailField(max_length = 200)
    message = models.TextField(
        blank = True
    )
    class ContactForm(ModelForm):
        class Meta:
           
            fields = ['your_email', 'message']
    
