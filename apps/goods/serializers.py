# -*- coding: utf-8 -*-
__author__ = 'Cribbee'
__create_at__ = 2018 / 3 / 31

from rest_framework import serializers

class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)