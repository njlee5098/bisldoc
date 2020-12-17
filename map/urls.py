from django.urls import path

from .views import map_views

app_name = 'map'

urlpatterns = [
    # map_views.py
    path('', map_views.map, name='map'),
]