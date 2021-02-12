from django import forms


class Contact(forms.Form):
    your_email = models.EmailField(max_length = 200)
    message = models.TextField(
        blank = True
    )
    class Meta:
        model = Contact,
        fields = ['your_email', 'message']
    
