from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.forms import forms
from .forms import UserRegistrationForm
# Create your views here.

class Home(View):
    def get(self,request,*args,**kwargs):
            return render(request, "home.html",)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.object.filter(username=username).exists() or User.object.filter(email=email).exists()):
                User.objects.create_user(username,email,password)
                user = authenticate(username=username, password=password)
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('User is already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})