from django.urls import path
from . import views

urlpaterns = [
    path('', views.product_list, name='product_list'),
]