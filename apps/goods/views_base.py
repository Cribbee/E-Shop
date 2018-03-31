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
        json_list = []
        goods = Goods.objects.all()[:10]#防止加载过慢，所以限制只获取10条
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     #json_dict["add_time"] = good.add_time #使用django所带的视图，会出现各种问题，比如datetime等类型字段无法json.dumps()成功序列化的
        #     json_list.append(json_dict)
        # 这样一个字段一个字段的取很费劲，所以可以利用django的"model_to_dict"方法，如下所示

        #from django.forms.models import model_to_dict

        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        #
        # # from django.http import HttpResponse
        # # import json
        # # return HttpResponse(json.dumps(json_list), content_type="application/json")

        """
        然而，seializer规定的格式是固定的，因此如果要加入更加灵活的restful接口处理，仅仅用django提供的view是不够的
        """
        import json
        #serializers 是model 不是方法，因此需要调用serialize方法进行json序列化
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data) #json.loads 与 json.dumps是相反作用的
        from django.http import HttpResponse, JsonResponse
        return JsonResponse(json_data, safe=False) #JsonResponse 会将dict字串转化为json格式 但无法处理str格式
