from django.urls import path
from . import views

urlpatterns = [
    path('', views.prog_day, name = 'prog_day'),
]