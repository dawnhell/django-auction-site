# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuctionApp', '0002_auto_20161105_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
