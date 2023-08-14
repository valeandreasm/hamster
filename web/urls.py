from django.contrib import admin
from django.urls import path
from web.views import sobre_mi, form


urlpatterns = [
    path('sobre_mi/', sobre_mi, name = 'Sobre mi'),
    path('form/', form, name = 'form')
]