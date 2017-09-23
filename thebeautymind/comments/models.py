from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
import misaka

from posts.models import Post
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey('posts.Post',on_delete=models.CASCADE,related_name='postcomments')
    author = models.ForeignKey(User,related_name='usercomments')
    text = models.TextField()
    text_html = models.TextField(editable=False,default='',blank=True)
    created_date = models.DateTimeField(default=timezone.now)


    def save(self,*args,**kwargs):
        self.text_html = misaka.html(self.text)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('comments:single',kwargs={'username':self.author.username,'pk':self.pk})

    def __str__(self):
        return self.text
