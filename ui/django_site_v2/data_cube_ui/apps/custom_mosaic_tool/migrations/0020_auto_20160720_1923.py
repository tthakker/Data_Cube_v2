# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_mosaic_tool', '0019_result_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='product_type',
            field=models.CharField(max_length=26),
        ),
    ]