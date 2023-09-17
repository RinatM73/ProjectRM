from django.urls import path
from . import views

urlpatterns = [
    path('', views.multip_table, name = 'multip_table'),
]