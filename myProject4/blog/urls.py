from django.urls import path
from . import views

urlpaterns = [
    path('', views.post_list, name='post_list'),
]