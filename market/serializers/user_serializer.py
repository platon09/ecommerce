from rest_framework import serializers
from market.models import UserProfile


class UserProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'name', 'get_small_image_url']