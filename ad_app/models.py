# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User as BaseUser
from categories.models import Category

# Create your models here.


class Ad(models.Model):
    class Meta:
        db_table = 'ad'
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'

    title = models.CharField(max_length=255, verbose_name='Наимениование')
    description = RichTextUploadingField(verbose_name='Описание')

    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=255, verbose_name='Город')

    category = models.ForeignKey(Category, verbose_name='Категория',
                                 help_text='<b style="color: #a2a6ab;">Вы можете выбрать сразу дочернюю категорию</b>')

    phone = models.CharField(max_length=255, verbose_name='Телефоны')

    location = models.ForeignKey('Coordinates', verbose_name='Метка на карте', null=True, blank=True)

    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Дата редактирования', auto_now=True)

    user = models.ForeignKey(BaseUser, verbose_name='Пользователь', null=True, blank=True)
    views = models.IntegerField(verbose_name='Просмотры', default=0, null=True, blank=True)

    price = models.IntegerField(default=0, verbose_name='Цена', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Coordinates(models.Model):
    class Meta:
        db_table = 'coordinates'
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'

    position = GeopositionField(verbose_name='Метка')

    def __unicode__(self):
        return str(self.position)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    body = RichTextUploadingField(verbose_name='Текст')
    user = models.ForeignKey(BaseUser, verbose_name='Пользователь')
    ad = models.ForeignKey('Ad', verbose_name='Объявление', null=True, blank=True)

    def __unicode__(self):
        return str(self.body)[:20]
