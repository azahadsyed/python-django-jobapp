from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from . import views


urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),

    # // added by me root url 
]
