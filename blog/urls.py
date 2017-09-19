from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # post/pk/; the pk can only be a digit \d; any n of digits +
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
