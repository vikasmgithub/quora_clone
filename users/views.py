from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import render
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name ='users/signup.html'
    success_url = reverse_lazy('question:test')