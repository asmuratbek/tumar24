# coding=utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<ad_id>[0-9]+)$', one_ad, name='one_ad'),
    url(r'^all$', all_ads, name='all_ads'),
    url(r'^create$', create_new_ad, name='create_new_ad'),
    url(r'^search$', search, name='search'),
    url(r'^upload/media$', upload_media, name='upload_media'),
    url(r'^upload/media/remove$', remove_uploaded_media, name='remove_uploaded_media')
]
