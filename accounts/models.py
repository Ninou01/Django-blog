from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.utils.text import slugify 
from django.db.models import signals
from django.conf import settings
from django.utils import timezone
import os

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000,blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    slug = models.SlugField(blank=True)
    img = models.ImageField(upload_to='userimg/',default='userimg/avatar.png')
    def __str__(self):
        return "%s" % self.user

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])
    

post_save.connect(create_profile, sender=User)

def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
        
signals.post_delete.connect(delete_user, sender=Profile)


