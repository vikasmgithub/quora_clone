from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from . import forms
from . import models
# Create your views here.
class QuestionList(LoginRequiredMixin, ListView):
    template_name = 'questions/question_list.html'

    def get_queryset(self):
        return models.Question.objects.filter(asked_by=self.request.user)


class QuestionDetail(LoginRequiredMixin, DetailView):
    template_name = 'questions/question_detail.html'

    def get_queryset(self):
        return models.Question.objects.all()


class AskQuestion(LoginRequiredMixin, CreateView):
    template_name = 'questions/question.html'
    form_class = forms.QuestionForm
    success_url = reverse_lazy('question:test')

    def form_valid(self, form):
        form.instance.asked_by = self.request.user
        return super(AskQuestion, self).form_valid(form)


class EditQuestion(LoginRequiredMixin, UpdateView):
    model = models.Question
    template_name = 'questions/question.html'
    form_class = forms.QuestionForm
    success_url = reverse_lazy('question:test')

    def get_object(self, *args, **kwargs):
        object = super(EditQuestion, self).get_object(*args, **kwargs)
        if object.asked_by != self.request.user:
            raise Http404('Not Allowed')
        return object

    def get_context_data(self, **kwargs):
        context = super(EditQuestion, self).get_context_data(*kwargs)
        question_title = self.get_object().title
        context['question_title'] = question_title
        return context