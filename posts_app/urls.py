# coding=utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^all$', all_posts, name='all_posts'),
    url(r'^(?P<post_id>[0-9]+)$', one_post, name='one_post'),
]
