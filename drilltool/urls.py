from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('rheology', drill, name='rheology'),
    path('ref', ref, name='refnote')
]
