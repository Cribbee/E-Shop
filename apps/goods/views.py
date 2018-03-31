from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
# Create your views here.


class GoodsListView(APIView):
    """
    List all goods
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)
