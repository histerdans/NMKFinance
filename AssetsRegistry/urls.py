from django.urls import path

from .views import new_AR

app_name = 'AssetsRegistry'
urlpatterns = [

    path('newAR/', new_AR, name='newAR'),
]
