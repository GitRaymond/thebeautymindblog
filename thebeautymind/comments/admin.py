from django.contrib import admin
from . import models
# Register your models here.
class CommentsInline(admin.TabularInline):
    model = models.Comment

admin.site.register(models.Comment)
