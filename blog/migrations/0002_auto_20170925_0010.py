# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-24 22:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 22, 10, 1, 337270, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 24, 22, 10, 1, 337270, tzinfo=utc)),
        ),
    ]
