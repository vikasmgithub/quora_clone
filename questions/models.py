from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.

class Question(models.Model):
	created_by = models.ForeignKey(User)
	title = models.TextField(max_length=20,null=True,blank=True)
	content = models.TextField(max_length=4000, null=True, blank=True)
	slug = AutoSlugField(populate_from='title')
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'{self.created_by} asked {self.title}'
