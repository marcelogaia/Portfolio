# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160402_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='language',
            field=models.ManyToManyField(to='website.Language'),
        ),
        migrations.AddField(
            model_name='resume',
            name='skill',
            field=models.ManyToManyField(to='website.Skill'),
        ),
    ]
