from django.contrib import admin

# models
from .models import Menu, Menu_item

admin.site.register(Menu)
admin.site.register(Menu_item)
