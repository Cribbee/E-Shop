# -*- coding: utf-8 -*-
__author__ = 'Cribbee'
__create_at__ = 2018 / 4 / 1


import django_filters

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    price_min = django_filters.NumberFilter(name='shop_price', help_text="最低价格",lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', help_text="最高价格",lookup_expr='lte')
    name = django_filters.CharFilter(name = 'name', lookup_expr='icontains')


    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']