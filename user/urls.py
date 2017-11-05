from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from .views import SignUp,UserFeed



urlpatterns = [
    url(r'^signup/$', SignUp.as_view(), name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^userfeed/$', UserFeed.as_view(), name='userfeed'),

]