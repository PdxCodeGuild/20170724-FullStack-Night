# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_text', models.CharField(max_length=500)),
                ('code_text', models.CharField(max_length=20)),
            ],
        ),
    ]
