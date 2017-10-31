from django.conf.urls import url

from django.views import generic

urlpatterns = [
    url(r'^test$', generic.TemplateView.as_view(template_name='../templates/layout.html'), name="test"),
]