# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsd', '0013_auto_20160902_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryOption',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
