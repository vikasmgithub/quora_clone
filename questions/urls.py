from django.conf.urls import url,include
from . import views



# from .views import IndexView

urlpatterns = [
    url(r'^list/$', views.QuestionListView.as_view(), name='list'),
    url(r'^detail/(?P<slug>[\w-]+)/$', views.QuestionDetailView.as_view(), name='detail'),
    url(r'^update/(?P<slug>[\w-]+)/$', views.QuestionUpdateView.as_view(), name='update'),
    url(r'^askquestion/$', views.AskQuestion.as_view(), name='question'),
    url(r'^like/(?P<pk>[0-9]+)$', views.like, name='like'),
    # url('^.*$', IndexView.as_view(), name='index'),
]