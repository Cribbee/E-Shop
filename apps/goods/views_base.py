# -*- coding: utf-8 -*-
__author__ = 'Cribbee'
__create_at__ = 2018 / 3 / 30

from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self,request):
        """
        通过Django的view实现商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]#防止加载过慢，所以限制只获取10条
