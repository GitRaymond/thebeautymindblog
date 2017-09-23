from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^posts/$',views.PostListView.as_view(),name='post_list'),
    url(r'^posts/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^posts/(?P<slug>[-\w]+)/$',views.PostSDetailView.as_view(),name='post_detail'),
    url(r'^posts/raymond/$',views.RaymondView.as_view(),name='raymond'),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^posts/(?P<slug>[-\w]+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),

    url(r'^posts/(?P<slug>[-\w]+)/publish/$',views.post_publish,name='post_publish'),
]
