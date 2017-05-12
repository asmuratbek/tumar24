from django.conf.urls import url
from .views import *


urlpatterns = [
    url('^not-found$', page_not_found, name='not_found'),
]
