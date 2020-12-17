from django.urls import path

from .views import pre_views

app_name = 'prescription'

urlpatterns = [
    # pre_views.py
    path('', pre_views.index, name='prescription'),
    path('upload/', pre_views.presc_upload, name='prescription_upload')
]