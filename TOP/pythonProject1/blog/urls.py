from django.urls import path
from . import views
urlpatterns = [
    path('', views.blogView, name = 'blog'),
    path('<int:article_id>/', views.detail, name = 'detail'),
]
