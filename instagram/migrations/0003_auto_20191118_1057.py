# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-18 07:57
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
