from rest_framework import serializers


class AddProductRequestSerializer(serializers.Serializer):
    cat = serializers.IntegerField(min_value=1)
    subcat = serializers.IntegerField(min_value=1)
    name = serializers.CharField()
    image = serializers.FileField(allow_empty_file=True, required=False)
    imager_base64 = serializers.CharField(required=False)