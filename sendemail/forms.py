from django import forms



class ContactForm(forms.Form):
    to_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': "newdlcntr@aol.com"}))
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)