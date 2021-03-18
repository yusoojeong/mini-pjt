from rest_framework import serializers
from .models import Restaurant
from .models import Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'price',)


class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'phone_number',)


class DetailSerializer(serializers.ModelSerializer):
    menus = serializers.StringRelatedField(many=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'discription', 'address', 'phone_number', 'menus',)