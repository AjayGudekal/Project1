# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-08-08 07:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnqDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('mno', models.IntegerField()),
                ('messege', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 8, 7, 44, 37, 518168, tzinfo=utc)),
        ),
    ]
