from django import forms


class Contact(forms.Form):
    your_email = forms.EmailField(max_length = 200)
    message = forms.CharField()
    class Meta:
        # model = Contact
        fields = ['your_email', 'message']
    
