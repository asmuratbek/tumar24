# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class VerticalBanners(models.Model):
    class Meta:
        verbose_name = 'вертикальный баннер'
        verbose_name_plural = 'Вертикальные баннеры'

    title = models.CharField(max_length=255, verbose_name='Наименование', null=True, blank=True)
    link = models.URLField(verbose_name='Внешняя ссылка')
    content = models.ImageField(upload_to='banners/vertical/', verbose_name='Картинка баннера')
    life_time = models.DateField(verbose_name='Время окончания', null=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.link


class HorizontalBanners(models.Model):
    class Meta:
        verbose_name_plural = 'Горизонтальные баннеры'
        verbose_name = 'горизонтальный баннер'

    title = models.CharField(max_length=255, verbose_name='Наименование', null=True, blank=True)
    link = models.URLField(verbose_name='Внешняя ссылка')
    content = models.ImageField(upload_to='banners/horizontal/', verbose_name='Картинка баннера')
    life_time = models.DateField(verbose_name='Время окончания', null=True)
    is_active = models.BooleanField(verbose_name='Активный', default=True)

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return self.link
