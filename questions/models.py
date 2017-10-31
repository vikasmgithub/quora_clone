from django.contrib.auth.models import User
from django.db import models

from autoslug import AutoSlugField
# Create your models here.
TAGS = (
    (0, 'Sports'),
    (5, 'Entertainment'),
    (10, 'Science'),
    (15, 'Politics'),
    (20, 'Environment'),
)

class Question(models.Model):
    asked_by = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=500, null=True, blank=True)
    tag = models.IntegerField(choices=TAGS)
    slug = AutoSlugField(populate_from='title', unique=True)
    asked_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.asked_by} asked {self.title}'