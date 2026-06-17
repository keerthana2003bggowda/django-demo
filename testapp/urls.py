from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.nature_info),
    path('flower/',views.flower_info),
    path('water/',views.water_info),
    path('temple/',views.temple_info),
]