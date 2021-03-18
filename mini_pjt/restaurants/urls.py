from django.urls import path
from . import views

app_name = 'restuarant'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('list/<int:page>/', views.index, name='list'),
    path('detail/<int:restaurant_id>/', views.detail, name='detail'),
    path('detail/<int:restaurant_id>/menu/create/', views.menu_create, name='menu_create'),
]
