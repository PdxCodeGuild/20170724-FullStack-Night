# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 02:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='question_text',
            new_name='todo_text',
        ),
    ]
