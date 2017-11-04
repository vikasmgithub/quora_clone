from django.contrib import admin

from .models import Question,Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','create_date','slug')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answered_by','create_date')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)