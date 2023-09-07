from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_user),
    path('register/', views.reg_user),
]