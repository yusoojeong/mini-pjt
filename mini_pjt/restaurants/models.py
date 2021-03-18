from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=25)                      # 음식점 이름
    description = models.CharField(max_length=200)              # 음식점 소개
    address = models.CharField(max_length=100)                  # 음식점 주소
    phone_number = models.CharField(max_length=13)              # 음식점 번호

class Menu(models.Model):
    name = models.CharField(max_length=20)                      # 메뉴 이름
    price = models.IntegerField()                               # 메뉴 가격
    restaurant = models.ForeignKey(                             # 음식점 id
                                    Restaurant,
                                    on_delete=models.CASCADE,
                                    related_name='menus'
                                    )
