
from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.Home,name='home'),
    path('confess/',views.confess,name='confess'),
]
