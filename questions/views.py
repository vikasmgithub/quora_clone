from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import Question,Answer,Vote
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from .forms import AnswerForm
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


class QuestionListView(ListView):
    template_name = 'listview.html'
    success_url = reverse_lazy('question:list')

    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset
    # def get_context_data(self, **kwargs):
    #     context = super(QuestionListView,self).get_context_data(**kwargs)
    #     context['answerform'] = AnswerForm
    #     context['action'] = reverse_lazy('question:comment')
    #     # print(context)
    #     return context




class QuestionDetailView(FormMixin,DetailView):
    template_name = 'detail.html'
    form_class = AnswerForm
    model = Question

    def vote(self):
        upvote_count = Vote.upvote
        down_vote = Vote.downvote


    def get_success_url(self):
        return reverse_lazy('question:detail', kwargs={'slug': self.object.slug})


    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView,self).get_context_data(**kwargs)
        context['answerform'] = AnswerForm(initial={'question': self.object, 'answered_by': self.request.user})
        # obj = get_object_or_404(Question,slug=self.kwargs['slug'])
        context['answer_list'] = Answer.objects.filter(question=self.object).order_by('create_date')
        # context['answer_list'] = obj.to_answer_set.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        print(form)
        form.save()
        return super(QuestionDetailView, self).form_valid(form)







class QuestionUpdateView(UpdateView):
    template_name = 'update.html'
    model = Question
    fields = ['title','content']
    success_url = reverse_lazy('question:list')

    def get_object(self, *args,**kwargs):
        object = super(QuestionUpdateView,self).get_object(*args,**kwargs)
        if object.created_by != self.request.user:
            raise Http404('Not allowed')
        return object




class AskQuestion(CreateView):
    template_name = 'question.html'
    model = Question
    success_url = reverse_lazy('question:list')
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.answered_by = self.request.user
        return super(AskQuestion,self).form_valid(form)

# class Answer (CreateView,DetailView):
#     template_name = 'answer.html'
#     form_class = AnswerForm
#     success_url = reverse_lazy('question:list')
#     model = Answer
#     # def get_queryset(self):
#     #     qs = Question.objects.filter(slug__exact=self.kwargs.get('slug'))
#     #     return qs
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(Answer, self).get_context_data(kwargs)
#     #     context['question'] = qs[0].content


def like(request,pk):
    new_vote, created = Vote.objects.get_or_create(user=request.user, question_id=pk)
    obj = get_object_or_404(Question,id=pk)
    slug = obj.slug
    return HttpResponse(reverse_lazy('question:detail'  , kwargs={'slug':slug}))
