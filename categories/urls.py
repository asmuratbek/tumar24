# coding=utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(
        r'^(?P<category>[-\w]+)$',
        parent_category,
        name='parent_category'
    ),
    url(
        r'^(?P<category>[-\w]+)/(?P<child>[-\w]+)$',
        child_category,
        name='child_category'
    )
]
