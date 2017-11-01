from django.conf.urls import url
from django.views import generic

from . import views

urlpatterns = [
    url(r'^test/$', generic.TemplateView.as_view(template_name='../templates/layout.html'), name="test"),
    url(r'^list/$', views.QuestionList.as_view(), name='list'),
    url(r'^ask/$', views.AskQuestion.as_view(), name='ask'),
    url(r'^detail/(?P<slug>[\w-]+)/$', views.QuestionDetail.as_view(), name='detail'),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.EditQuestion.as_view(), name='edit'),
]