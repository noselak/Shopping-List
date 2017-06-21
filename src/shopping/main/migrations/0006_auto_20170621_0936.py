# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_shoppingitem_bought'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shoppingitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='shoppingitem',
            name='shopping_list',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ShoppingItem',
        ),
        migrations.DeleteModel(
            name='ShoppingList',
        ),
    ]
