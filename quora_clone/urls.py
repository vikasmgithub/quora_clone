"""quora_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from questions import urls as questionurl
from .views import Home
from user import urls as userurl
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^question/', include(questionurl, namespace='question')),
    url(r'^user/', include(userurl, namespace='user')),
    # url(r'^l/$', Home,   name='list'),
    url(r'^test/$', generic.TemplateView.as_view(template_name='base.html'), name="test"),

]
