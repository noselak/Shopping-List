# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shoppingitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='shop',
            field=models.CharField(max_length=15),
        ),
    ]
