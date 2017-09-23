from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import misaka

from django.contrib.auth import get_user_model
User=get_user_model()


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,related_name='posts')
    title = models.CharField(max_length=400)
    slug = models.SlugField(allow_unicode=True,unique=True,default='')
    second_title = models.CharField(max_length=400)
    text = models.TextField()
    text_html = models.TextField(editable=False,default='',blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        self.text_html = misaka.html(self.text)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("posts:detail",kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['title']    

class PostImages(models.Model):
    post = models.ForeignKey(Post,related_name='postimage')
    image = models.ImageField(upload_to='post_pics',blank=True)
