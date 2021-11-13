from rest_framework import serializers
from market.views.category_view import CategorySerializer
from market.views.subcategory_view import SubCategorySerializer
from market.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    subcategory = SubCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory', 'get_small_image_url']
