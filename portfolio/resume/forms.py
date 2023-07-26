from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    full_name = forms.CharField(max_length= 50, required = True)
    email = forms.EmailField(required = True)
    subject = forms.CharField(max_length= 100, required = True)
    message = forms.CharField(max_length= 1000, required = True)
  
    
    class Meta:
        model = Message
        exclude = []
