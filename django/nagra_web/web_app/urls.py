from django.contrib import admin
from django.urls import path
from web_app import views

urlpatterns = [
    path('home/',views.index,name='home'),
    path('form/',views.form,name='form')  ]
