from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from . import views


urlpatterns = [
    path('image/', views.upload_image, name='upload_image'),
    # // added by me root url
    path('file/', views.upload_file, name='upload_file'),
]
