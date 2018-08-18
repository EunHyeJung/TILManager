from django.urls import path
from . import views


urlpatterns = [
    path('tils', views.til_list, name = 'til_list'),
    path('tils/<int:pk>', views.til_detail, name = 'til_detail'),
    path('til_new', views.til_new, name = 'til_new'),
]