# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dsd', '0008_auto_20160831_0836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='besmiddlewarecore',
            old_name='cases_anger',
            new_name='cases_rabies',
        ),
        migrations.RenameField(
            model_name='besmiddlewarecore',
            old_name='deaths_anger',
            new_name='deaths_rabies',
        ),
        migrations.RenameField(
            model_name='besmiddlewarecore',
            old_name='note_anger',
            new_name='note_rabies',
        ),
    ]
