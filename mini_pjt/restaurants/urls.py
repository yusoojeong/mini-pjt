from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('menu/create/', views.menu_create, name='menu_create'),
    path('page/<int:page>/', views.page, name='page'),
    path('page/<int:page>/detail/', views.detail, name='detail'),
    path('page/<int:rest_id>/menu/<int:menu_id>/', views.menu_add, name='menu_add'),
]
