# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sagyurl',
            name='shortcode',
            field=models.CharField(default='admindefaultshortcode', max_length=20),
            preserve_default=False,
        ),
    ]