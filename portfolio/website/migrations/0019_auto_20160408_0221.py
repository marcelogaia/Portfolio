# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20160408_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_image',
            name='image',
            field=models.ImageField(upload_to='project-pictures'),
        ),
    ]
