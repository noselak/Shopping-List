# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_shoppinglist_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]