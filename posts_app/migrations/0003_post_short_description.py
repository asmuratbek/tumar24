# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_auto_20170512_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description',
            field=models.TextField(max_length=1000, null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
    ]
