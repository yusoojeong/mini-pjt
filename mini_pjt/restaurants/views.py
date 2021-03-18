from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer


# 음식점 Create
def create(request):
    pass


# 음식점 목록
def index(request, page):
    pass


# 음식점 자세한 내용
def detail(request, restaurant_id):
    pass


# 음식점의 메뉴 Create
def menu_create(request, restaurant_id):
    pass