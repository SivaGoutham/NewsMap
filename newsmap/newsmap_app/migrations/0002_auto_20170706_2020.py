# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsmap_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
