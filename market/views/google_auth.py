from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema

from market.models import UserProfile
import requests
from config.settings import BASE_DIR
from django.core.files import File
from market.serializers.user_serializer import UserProfileSerializer

from market.serializers.google_auth_serializer import GoogleAuthRequestSerializer
from rest_framework.authtoken.models import Token


class GoogleView(APIView):
    """
    Авторизация через Google.
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=GoogleAuthRequestSerializer
    )
    def post(self, request, format=None):

        try:
            user = UserProfile.objects.get(username=request.data['email'])
            token = Token.objects.get(user=user)
        except:
            user = UserProfile()
            user.username = request.data['email']
            user.is_active = True
            user.set_password('123')
            user.save()
            token = Token.objects.create(user=user)

            r = requests.get(request.data['photoUrl'], stream=True)
            if r.status_code == 200:
                filename = '%s/tmp.jpg' % BASE_DIR
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                with open(filename, 'rb') as image:
                    user.image.save('%s.jpeg' % user.id, File(image))

        return Response({
            'token': token.key,
            'agent': request.META['HTTP_USER_AGENT'],
            'user': UserProfileSerializer(user).data
        })
