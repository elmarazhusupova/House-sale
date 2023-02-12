from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contacts', contact, name='contacts'),
    path('price', price, name='price'),
    path('house', house, name='house'),
    path('listof/', listof, name='listof')
]