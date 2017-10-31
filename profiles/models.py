from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    User = models.OneToOneField()
    Bio = models.CharField(max_length=50,required=True)
    activated = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

def  post_save_user_reciever(sender,intance,created,*args,**kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)
