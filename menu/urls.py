# coding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<menu_name>[0-z]+)/$', views.show_single_menu, name='show_single_menu'),
    url(r'^(?P<menu_name>[0-z]+)/(?P<active_item>[0-z]+)/$', views.show_menu_w_active_item, name='show_menu_w_active_item'),
    url(r'^', views.show_menu, name='show_menu'),
]
