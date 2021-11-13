from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from django.core.files.base import ContentFile
import base64

from market.serializers.add_product_serializer import AddProductRequestSerializer

from market.models import Product, Category, SubCategory


class AddProductView(APIView):
    """
    Adding a new product.
    """
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        cat = Category.objects.get(pk=request.data.get('cat'))
        subcat = SubCategory.objects.get(pk=request.data.get('subcat'))

        p = Product()
        p.category = cat
        p.subcategory = subcat
        p.name = request.data.get('name')
