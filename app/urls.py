from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# from app.views import hello
# from app.views import jobPage
# from app import views
from . import views

urlpatterns = [
    # path('',hello),
    # path('job/1',jobPage),
    path('', views.jobList, name='jobs_home'),
    path('hello/', views.hello, name='hello'),
    path('job/<int:id>', views.jobPage, name='jobs_detail'),

]
