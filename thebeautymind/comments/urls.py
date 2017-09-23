from django.conf.urls import url
from . import views

app_name = 'comments'

urlpatterns = [
        url(r'^comments/(?P<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
]
