from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=250)
    img_link =models.CharField(max_length=3000, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)