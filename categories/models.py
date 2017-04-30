# coding=utf-8
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.CharField(max_length=225, verbose_name='Slug', null=True)
    parent = models.ForeignKey('Category', verbose_name='Родительская категория', null=True, blank=True)
    description = RichTextUploadingField(verbose_name='Описание категории', null=True, blank=True)
    meta_title = models.CharField(max_length=255, verbose_name='Meta наименование', null=True, blank=True)
    meta_description = models.CharField(max_length=255, verbose_name='Meta Описание', null=True, blank=True)
    meta_key_words = models.CharField(max_length=255, verbose_name='Meta Ключевые слова', null=True, blank=True,
                                      help_text='<b style="color: #a2a6ab;">Вводить через запятую</b>')

    def save(self, *args, **kwargs):
        self.meta_title = self.title
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
