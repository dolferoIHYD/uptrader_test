# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 18:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menu_item_id_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_item',
            name='id_path',
        ),
    ]
