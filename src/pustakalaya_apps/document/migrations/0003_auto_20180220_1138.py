# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 05:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20180220_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='document.DocumentSeries', verbose_name='Series'),
        ),
    ]