# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-28 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170628_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynews',
            name='mobileurl',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mynews',
            name='weburl',
            field=models.CharField(max_length=200),
        ),
    ]
