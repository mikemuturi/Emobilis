from django import forms

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    image = forms.ImageField(required=False)
