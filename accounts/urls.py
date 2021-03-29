from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from .views import register_page, login_page, logout_user

app_name = 'accounts'
urlpatterns = [

    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_page, name='register'),
]
