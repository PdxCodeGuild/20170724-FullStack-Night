# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 03:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainex', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RenameModel(
            old_name='UserSkills',
            new_name='UserSkill',
        ),
    ]