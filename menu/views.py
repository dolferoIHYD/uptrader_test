# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import *

def show_single_menu(request, menu_name):
    # эта вьюха показывает одно меню без выделенных элементов

    try:
        menu = Menu.objects.get(title = menu_name)
    except Menu.DoesNotExist:
        return HttpResponse("Нет меню с таким названием")

    menu_items = Menu_item.objects.filter(menu=menu, level=1)
    return render(request, 'show_single_menu.html', {
        'menu': menu,
        'first_level_items': menu_items,
    })

def show_menu_w_active_item(request, menu_name, active_item):
    # вьюха возвращает шаблон с активной ячейкой,
    # на вход принимает название меню и название активной ячейки

    # проверяем, верные ли параметры переданы в URL
    try:
        menu = Menu.objects.get(title = menu_name)
    except Menu.DoesNotExist:
        return HttpResponse("Нет такого меню")

    try:
        a_item = Menu_item.objects.get(title = active_item)
    except Menu_item.DoesNotExist:
        return HttpResponse("Нет такого пункта меню")


    child = list(Menu_item.objects.filter(parent_item = a_item))
    if child:
        print(child)
        this_list = child
        answer_list = list(Menu_item.objects.filter(parent_item=a_item.parent_item))
        # ищем место родителя в списке
        for i in range(len(answer_list)):
            if answer_list[i] == a_item:
                p_ind = i+1
                break
        # вставляем поэлементно подсписок в список
        for item in this_list:
            answer_list.insert(p_ind, item)
            p_ind += 1
    else:
        answer_list = list(Menu_item.objects.filter(parent_item=a_item.parent_item))

    this_item = a_item.parent_item
    for i in range(a_item.level-1, 0, -1):
        this_list = answer_list
        answer_list = list(Menu_item.objects.filter(parent_item = this_item.parent_item))
        # ищем место родителя в списке
        for i in range(len(answer_list)):
            if answer_list[i] == this_item:
                p_ind = i+1
                break
        # вставляем поэлементно подсписок в список
        for item in this_list:
            answer_list.insert(p_ind, item)
            p_ind += 1
        this_item = this_item.parent_item

    return render(request, "show_menu_w_active_item.html", {
        'list': answer_list,
        'menu': menu,
    })

def show_menu(request):
    return render(request, "show_menu.html")
