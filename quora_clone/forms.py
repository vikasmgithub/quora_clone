from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=32,required=True,label='Username')
    email = forms.CharField(max_length=32,required=True,label='Email')
    password = forms.CharField(max_length=32,required=True,label='Password',widget=forms.PasswordInput)