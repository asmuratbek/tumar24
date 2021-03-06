# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-10 12:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.CharField(max_length=225, null=True, verbose_name='Slug')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435')),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta \u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('meta_key_words', models.CharField(blank=True, help_text='<b style="color: #a2a6ab;">\u0412\u0432\u043e\u0434\u0438\u0442\u044c \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e</b>', max_length=255, null=True, verbose_name='Meta \u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category', verbose_name='\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
    ]
