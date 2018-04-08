# -*- coding: utf-8 -*-
__author__ = 'Cribbee'
__create_at__ = 2018 / 3 / 31

from rest_framework import serializers
from datetime import datetime

from goods.models import Goods,  GoodsCategory

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#     add_time = serializers.DateTimeField(default=datetime.now)


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)  # 由于一个主类别下面对应多个2级类，因此不要漏写many=True

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # 这里实例化，完成Serializer的嵌套，将从属关系也序列化完成展示

    class Meta:
        model = Goods
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new instance, given the validated data.
        :param validated_data:
        :return:
        """
        return Goods.objects.create(**validated_data)