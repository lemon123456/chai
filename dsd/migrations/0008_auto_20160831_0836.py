# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 08:36
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dsd', '0007_element'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syncrecord',
            name='last_sync_time',
        ),
        migrations.AddField(
            model_name='syncrecord',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='syncrecord',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='syncrecord',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='Not_running', max_length=100, no_check_for_status=True),
        ),
    ]
