# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-07 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hive', '0005_academicapplying'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicapplying',
            old_name='phone',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='academicapplying',
            old_name='college',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='academicapplying',
            old_name='first',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='academicapplying',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='academicapplying',
            name='language',
        ),
        migrations.RemoveField(
            model_name='academicapplying',
            name='last',
        ),
        migrations.RemoveField(
            model_name='academicapplying',
            name='level',
        ),
    ]
