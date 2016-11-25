# coding: utf-8
from django import template
from menu.models import Menu, Menu_item

register = template.Library()

@register.inclusion_tag('show_single_menu.html')
def show_menu(name):
    # эта вьюха показывает одно меню без выделенных элементов
    try:
        menu = Menu.objects.get(title = name)
    except Menu.DoesNotExist:
        return HttpResponse("Нет меню с таким названием")

    menu_items = Menu_item.objects.filter(menu=menu, level=1)
    print ('here')
    return {
        'menu': menu,
        'first_level_items': menu_items,
    }
