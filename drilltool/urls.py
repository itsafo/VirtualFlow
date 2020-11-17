from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    path('rheology', drill, name='rheology'),
    path('reinforcement', BRF, name='reinforcement'),
    path('ref', ref, name='refnote')
]
