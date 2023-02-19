from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contacts', contact, name='contacts'),
    path('price', price, name='price'),
    path('house', house, name='house'),
    path('house_post/', house_post, name='house_post'),
    path('<int:id>', views.detail_page, name='detail'),
]
