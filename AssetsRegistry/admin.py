from django.contrib import admin
from .models import AssetsRegistry, Department, Account, Station, Item

admin.site.register(AssetsRegistry)
admin.site.register(Account)
admin.site.register(Department)
admin.site.register(Station)
admin.site.register(Item)
