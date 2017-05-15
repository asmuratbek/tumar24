# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Post(models.Model):
    class Meta:
        verbose_name = u'пост'
        verbose_name_plural = u'Новости'

    title = models.CharField(max_length=255, verbose_name='Наименование')
    short_description = models.TextField(max_length=300, verbose_name='Краткое описание новости', null=True, blank=True,
                                         help_text='<b>Максимум 300 символов. На главной странице выводится только 128 символов</b>')
    text = RichTextUploadingField(verbose_name='Текст статьи')
    views = models.IntegerField(verbose_name='Просмотры', null=True, blank=True, default=0)

    preview = models.ForeignKey('ad_app.Media', verbose_name='Главгая картинка')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    def __unicode__(self):
        return self.title

