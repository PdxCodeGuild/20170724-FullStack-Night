# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brainex', '0009_userskill_teach_boolean'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='fk_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='brainex.Skill'),
        ),
    ]
