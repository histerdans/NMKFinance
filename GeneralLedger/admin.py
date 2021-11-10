from django.contrib import admin

from .models import GeneralLedger, Category, Item, DepartmentGeneralLedger, Department, Station

admin.site.register(GeneralLedger)
admin.site.register(DepartmentGeneralLedger)
admin.site.register(Department)
admin.site.register(Station)
admin.site.register(Category)
admin.site.register(Item)

