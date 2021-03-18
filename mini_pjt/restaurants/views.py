from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer


# 음식점 Create
@api_view(['POST'])
def create(request):
    serializer = RestaurantSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

        return Response(serializer.data)


# 음식점 목록
@api_view(['GET'])
def index(request, page):
    restaurant = get_object_or_404(Restaurant, pk=page)
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)


# 음식점 자세한 내용
@api_view(['GET'])
def detail(request, restaurant_id):
    pass


# 음식점의 메뉴 Create
@api_view(['POST'])
def menu_create(request, restaurant_id):
    pass