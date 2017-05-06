# coding=utf-8
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(
        r'^logout$',
        users_logout,
        name='users_logout'
    ),
    url(
        r'^login$',
        users_login,
        name='users_login'
    ),
    url(
        r'^register$',
        users_register,
        name='users_register'
    ),
    url(
        r'^email/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/(?P<password>[0-9A-Za-z_\-]+)$',
        users_email_confirm,
        name='users_confirm'
    ),
    url(
        r'^email/confirm/result/(?P<success>[-\w]+)$',
        users_email_confirm_result,
        name='users_confirm_result'
    ),
]
