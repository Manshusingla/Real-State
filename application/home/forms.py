from django import forms

class Contact(forms.Form):
    first_name=forms.CharField(max_length=100,label="first name")
    last_name=forms.CharField(max_length=100,label="last name")
    email=forms.CharField(max_length=100,label="your email")
    phone=forms.IntegerField(label="your phone")
    message=forms.CharField(max_length=100,label="Message")
