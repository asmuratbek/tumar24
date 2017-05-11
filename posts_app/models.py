# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = u'пост'
        verbose_name_plural = u'Посты'

    pass
