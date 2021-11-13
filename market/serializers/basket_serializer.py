from rest_framework import serializers


class BasketRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(min_value=1))
