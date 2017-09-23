from django.views import generic
from comments.models import Comment
from comments.forms import CommentForm

from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404,redirect

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.


@login_required
def comment_remove(request,pk,*args,**kwargs):
    comment = get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('posts:post_detail', slug=comment.post.slug)
