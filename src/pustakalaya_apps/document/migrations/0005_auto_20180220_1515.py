# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_auto_20180220_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='published',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', max_length=3, verbose_name='published'),
        ),
    ]
