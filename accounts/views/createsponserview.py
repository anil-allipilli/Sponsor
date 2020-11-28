
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
from accounts.serializers import (
    SponserSerializer,
    MyTokenObtainPairSerializer,
    UserSerializer
)
from accounts.models import Sponsee, User, School, Reason, Sponser, Sponsee

from rest_framework.settings import api_settings
from rest_framework_simplejwt import views as jwt_views


class CreateSponserView(CreateAPIView):

    def create(self, request):
        serializer = UserSerializer(data={
            "username": request.data.get("username"),
            "password": request.data.get("password"),
            "first_name": request.data.get("firstName"),
            "last_name": request.data.get("lastName"),
            "email": request.data.get("email"),
        })
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()
        new_sponser = Sponser.objects.create(user=new_user)
        headers = self.get_success_headers(
            SponserSerializer(new_sponser).data)
        return Response(SponserSerializer(new_sponser).data, headers=headers)


class MyTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
