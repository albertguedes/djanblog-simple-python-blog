# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=256)
    email = forms.EmailField()
    subject = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea)
