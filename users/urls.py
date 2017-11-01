from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name':'users/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name':'users/logged_out.html'} ,name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url(r'^admin/', admin.site.urls),
]