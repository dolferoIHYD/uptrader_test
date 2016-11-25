# coding: utf-8
from __future__ import unicode_literals

from django.db import models

class Menu(models.Model):
    # модель меню
    title = models.CharField(max_length=20, default='Default_menu_name', blank=False)

    def __str__(self):
        return self.title
        

class Menu_item(models.Model):
    # модель элемента меню (узла)
    menu = models.ForeignKey(Menu)
    level = models.IntegerField(default=1)
    parent_item = models.ForeignKey('self', null=True, default=None, blank=True)
    title = models.CharField(max_length=20, default='Default_item_name', blank=False)

    def __str__(self):
        return self.title
