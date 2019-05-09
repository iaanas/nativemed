from django.urls import path
from acomapp.views import base_view

urlpatterns = [
    path('', base_view, name='base'),
]
