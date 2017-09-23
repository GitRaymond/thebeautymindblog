from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views import generic
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from comments.forms import CommentForm
# Create your views here.

class PostSDetailView(generic.DetailView):
    model = Post

    def get_context_data(self,**kwargs):
        context = super(PostSDetailView,self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self,request, *args, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', slug=self.kwargs['slug'])
        return redirect('posts:post_detail', slug=self.kwargs['slug'])


class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class RaymondView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class CreatePostView(LoginRequiredMixin,generic.CreateView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_list.html'

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')

class DraftListView(LoginRequiredMixin,generic.ListView):
    login_url = '/login/'
    redirect_field_name = 'posts/post_list.html'

    template_name = 'posts/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('posts:detail', slug=slug)
