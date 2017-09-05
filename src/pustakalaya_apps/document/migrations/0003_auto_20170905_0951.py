# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_item_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='item_Collection',
            field=models.ManyToManyField(to='collection.Collection', verbose_name='Add to these collections'),
        ),
    ]
