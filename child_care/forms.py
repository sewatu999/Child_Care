from django import forms


class Contact(forms.Form):
    your_email = forms.EmailField(max_length = 200)
    message = forms.CharField(widget=forms.Textarea)  
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False) 
    class Meta:
        # model = Contact
        fields = ['your_email', 'message', 'sender', 'cc_myself']
    
