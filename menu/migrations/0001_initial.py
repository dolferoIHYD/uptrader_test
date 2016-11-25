# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Default_menu_name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('title', models.CharField(default='Default_item_name', max_length=20)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu')),
                ('parent_item', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu_item')),
            ],
        ),
    ]
