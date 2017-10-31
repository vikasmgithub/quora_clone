from django.shortcuts import render

# Create your views here.

class RegisterView(CreateView):
    form_class =
    template_name =
    succes_url = '/'

    def dispatch(self,*args,*kwargs):
        return super(RegisterView,self).dispatch(*args,**kwargs)