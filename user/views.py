
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.




class SignUp(CreateView):
    template_name ='registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

