from django.contrib import admin
from .models import AssetsRegistry, Category, Item, ItemType, Department, DepartmentItem

admin.site.register(AssetsRegistry)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(ItemType)
admin.site.register(Department)
admin.site.register(DepartmentItem)
