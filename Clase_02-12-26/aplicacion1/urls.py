from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('tutorial/', views.vista_tutorial, name='tutorial'),
    path('tutorial-1/', views.vista_tutorial_1, name='tutorial-1'),
    path('tutorial-2/', views.vista_tutorial_2, name='tutorial-2'),
]