from django.urls import path
from . import views

urlpatterns = [
    path('', views.date_time, name = 'date_time'),
]