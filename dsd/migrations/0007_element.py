# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsd', '0006_auto_20160830_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.CharField(max_length=225, primary_key=True, serialize=False, unique=True)),
                ('aggregation_type', models.CharField(max_length=225, null=True)),
                ('domain_type', models.CharField(max_length=225, null=True)),
                ('value_type', models.CharField(default='', max_length=255)),
                ('code', models.CharField(default='', max_length=255)),
                ('name', models.CharField(default='', max_length=255)),
                ('short_name', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
