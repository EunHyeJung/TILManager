from django.urls import path
from . import  views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('posts/', views.post_new, name = 'post_new'),
    path('posts/<int:pk>', views.post_detail, name = 'post_detail'),
]