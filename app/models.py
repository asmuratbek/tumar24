# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from geoposition.fields import GeopositionField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Metro(models.Model):
    class Meta:
        verbose_name_plural = 'Станции метро'
        verbose_name = 'станцию метро'

    title = models.CharField(max_length=255, verbose_name='Название')
    location = GeopositionField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class City(models.Model):
    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'Города'

    title = models.CharField(max_length=255, verbose_name='Название')

    def __unicode__(self):
        return self.title


class AboutUs(models.Model):
    class Meta:
        verbose_name_plural = 'О нас'
        verbose_name = 'о нас'

    title = models.CharField(max_length=255, default='Редактирование страницы о нас')
    text = RichTextUploadingField(verbose_name='Страница о нас')

    def __unicode__(self):
        return self.title
