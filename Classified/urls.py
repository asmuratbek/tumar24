# coding=utf-8
"""Classified URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from Classified import settings
from app import views as app_views

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', app_views.index, name='index'),
    url(r'^category/', include('categories.urls', namespace='categories')),
    url(r'^fixtures/(?P<thread>\w+)$', app_views.fixtures, name='fixtures'),
    url(r'^ad/', include('ad_app.urls', namespace='ad')),
    url(r'^user/', include('users_app.urls', namespace='users')),
    url(r'^news/', include('posts_app.urls', namespace='news')),
    url(r'^exception/', include('tumar_exceptions.urls', namespace='exception')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
