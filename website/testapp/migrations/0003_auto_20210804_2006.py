# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-08-04 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20210804_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ejob',
            field=models.CharField(max_length=30),
        ),
    ]
