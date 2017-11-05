from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from questions import models
from django.core.urlresolvers import reverse_lazy

# Create your views here.




class SignUp(generic.CreateView):
    template_name ='registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

class UserFeed(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'userfeed.html'
    success_url = reverse_lazy('question:list')
    model = models.Question