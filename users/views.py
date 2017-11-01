from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from questions import models
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name ='users/signup.html'
    success_url = reverse_lazy('question:test')


class UserFeed(LoginRequiredMixin, generic.ListView):
    template_name = 'feed/question_feed.html'
    model = models.Question