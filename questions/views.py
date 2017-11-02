from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Question
from django.core.urlresolvers import reverse_lazy



class QuestionListView(ListView):
    template_name = 'listview.html'
    success_url = reverse_lazy('question:list')

    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset

class QuestionDetailView(DetailView):
    template_name = 'detaileview.html'

    def get_queryset(self):
        return Question.objects.all()


class AskQuestion(CreateView):
    template_name = 'question.html'
    model = Question
    success_url = reverse_lazy('question:list')
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AskQuestion,self).form_valid(form)