from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:page>/', views.page, name='page'),
    path('<int:page>/detail/', views.detail, name='detail'),
    path('<int:page>/menu/create/', views.menu_create, name='menu_create'),
]
