from django.forms import ModelForm
from .models import Question,Answer
from django import forms

class QuestionForm(ModelForm):
        class Meta:
            model = Question
            fields = ['title', 'content',]



class AnswerForm(ModelForm):
        class Meta:
            model = Answer
            fields = ('answer', 'question', 'answered_by')
            widgets = {'question': forms.HiddenInput(), 'answered_by': forms.HiddenInput()}