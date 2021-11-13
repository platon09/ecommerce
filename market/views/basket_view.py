from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from market.models import Product
from market.serializers.basket_serializer import BasketRequestSerializer
from market.serializers.product_serializer import ProductSerializer


class BasketInfoView(APIView):
    """
    Получение информации о товарах в корзине
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=BasketRequestSerializer
    )
    def post(self, request, format=None):
        out = []
        for item in request.data['ids']:
            out.append(ProductSerializer(Product.objects.get(pk=item)).data)
        return Response(out)
