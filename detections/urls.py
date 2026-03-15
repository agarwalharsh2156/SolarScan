from django.urls import path
from .views import process_map_click, map_interface

urlpatterns = [
    path('map/', map_interface, name='map_interface'), 
    path('api/analyze/', process_map_click, name='analyze_map'),
]