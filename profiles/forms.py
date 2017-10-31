from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(max_length=32,label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32,label='Password Confirm',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email',)

    def clean_email(self):

