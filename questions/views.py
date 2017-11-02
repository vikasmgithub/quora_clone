from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import Question
from django.http import Http404
from django.core.urlresolvers import reverse_lazy



class QuestionListView(ListView):
    template_name = 'listview.html'
    success_url = reverse_lazy('question:list')

    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset

class QuestionDetailView(DetailView):
    template_name = 'detail.html'

    def get_queryset(self):
        return Question.objects.all()

class QuestionUpdateView(UpdateView):
    template_name = 'update.html'
    model = Question
    fields = ['title','content']
    success_url = reverse_lazy('question:list')

    def get_object(self, *args,**kwargs):
        object = super(QuestionUpdateView,self).get_object(*args,**kwargs)
        if object.created_by != self.request.user
            raise Http404('Not allowed')
        return object


class AskQuestion(CreateView):
    template_name = 'question.html'
    model = Question
    success_url = reverse_lazy('question:list')
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AskQuestion,self).form_valid(form)