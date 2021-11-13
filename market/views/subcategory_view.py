from rest_framework import viewsets
from rest_framework import permissions

from market.models import SubCategory
from market.serializers.subcategory_serializer import SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """"
        API endpoint that allows users to read and modify categories
    """
    queryset = SubCategory.objects.all().order_by('-id')
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', ]
