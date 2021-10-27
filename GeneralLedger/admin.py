from django.contrib import admin

from .models import GeneralLedger, Category, Item

admin.site.register(GeneralLedger)
admin.site.register(Category)
admin.site.register(Item)

