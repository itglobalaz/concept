from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)