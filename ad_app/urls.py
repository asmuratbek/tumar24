# coding=utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^(?P<ad_id>[0-9]+)$', one_ad, name='one_ad'),
]
