import datetime
from django.db import models
from accounts.models import Profile
from django.utils.text import slugify 

# Create your models here.

class Post(models.Model):
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    creation_date = models.DateTimeField(default=datetime.datetime.now()) 
    tags = models.CharField(max_length=30, blank=True)
    # category
    public = models.BooleanField(default=True)
    img = models.ImageField(upload_to='postimg/',blank=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

        

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        lst = self.text.split()
        if len(lst) >=6 :
            return " ".join(lst[:5]) + '...'
        else:
            return self.text
    