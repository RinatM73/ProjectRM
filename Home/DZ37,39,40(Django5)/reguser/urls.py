from django.urls import path
from .views import *

urlpatterns = [
    path('register/', reguserview, name = 'reguser')
]
