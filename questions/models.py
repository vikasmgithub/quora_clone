from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
	created_by = models.ForeignKey(User)
	title = models.CharField(max_length=255)
	content = models.TextField(max_length=4000, null=True, blank=True)
	slug = models.SlugField(unique=True)
	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(blank=True, null=True)
