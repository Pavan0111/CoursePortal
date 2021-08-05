from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.courseshome, name='courseshome'),
    path('courseshome/<int:id>', views.courseshome, name='courseshome'),
    path('<str:slug>', views.coursesPost, name='coursesPost'),

]
