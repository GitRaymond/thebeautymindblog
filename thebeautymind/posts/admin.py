from django.contrib import admin
from . import models

# Register your models here.
class PostsInline(admin.TabularInline):
    model = models.Post

admin.site.register(models.Post)
