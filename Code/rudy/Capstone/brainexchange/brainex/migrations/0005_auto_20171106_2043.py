# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brainex', '0004_auto_20171106_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='skill',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
