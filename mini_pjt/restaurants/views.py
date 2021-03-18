from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse 

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Restaurant, Menu
from .serializers import RestaurantSerializer, MenuSerializer, ReadSerializer, DetailSerializer

@api_view(['GET'])
def index(request):
    restaurants = Restaurant.objects.all().order_by('pk')
    serializer = ReadSerializer(restaurants, many=True)
    return Response(serializer.data)

# 음식점 Create
@api_view(['POST'])
def create(request):
    serializer = RestaurantSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

        return Response(serializer.data)


# 음식점 목록
@api_view(['GET'])
def page(request, page):
    restaurant = get_object_or_404(Restaurant, pk=page)
    serializer = ReadSerializer(restaurant)
    return Response(serializer.data)


# 음식점 detail
@api_view(['GET'])
def detail(request, page):
    restaurant = get_object_or_404(Restaurant, pk=page)
    serializer = DetailSerializer(restaurant)
    return Response(serializer.data)


# 음식점의 메뉴 Create
@api_view(['POST'])
def menu_create(request, page):
    serializer = MenuSerializer(data=request.data)
    restaurant = get_object_or_404(Restaurant, pk=page)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(restaurant=restaurant)

        return Response(serializer.data)