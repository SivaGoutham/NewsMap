# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmap_app', '0002_auto_20170706_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.CharField(max_length=100),
        ),
    ]
