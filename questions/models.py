from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

class Question(models.Model):
	created_by = models.ForeignKey(User)
	title = models.TextField(max_length=20,null=True,blank=True)
	content = models.TextField(max_length=4000, null=True, blank=True)
	upvotes = models.IntegerField(blank=True, null=True)
	downvote = models.IntegerField(blank=True, null=True)
	slug = AutoSlugField(populate_from='title',unique=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'{self.created_by} asked {self.title}'


class Answer(models.Model):
	answered_by = models.ForeignKey(User)
	question = models.ForeignKey(Question,related_name='to_answer')
	answer = models.TextField(max_length=400,null=True,blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'{self.answered_by}'

class Vote(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	created = models.DateTimeField(auto_now_add=True)


