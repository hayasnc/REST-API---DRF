# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-30 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190830_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
