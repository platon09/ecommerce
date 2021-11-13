from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Product
from market.filters import ProductFilter

from market.serializers.product_serializer import ProductSerializer


class ProductListView(ListModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
