# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_app', '0003_remove_ad_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0435 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0435?'),
        ),
    ]