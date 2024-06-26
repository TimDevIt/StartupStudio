import markdownx
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'MyProfile'
urlpatterns = [
    path('', views.get_profile, name='get_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]