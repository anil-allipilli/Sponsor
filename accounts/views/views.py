from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
from accounts.serializers import SponseeCreateSerializer, SponserCreateSerializer, ReasonSerializer, SchoolSerializer, SponseeListSerializer, MyTokenObtainPairSerializer
from accounts.models import Sponsee, User, School, Reason, Sponser, Sponsee
from accounts.permissions import IsOwnerOrSponsorStaffReadOnly
from rest_framework.settings import api_settings
from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import IsAuthenticated


class CreateSponserView(CreateAPIView):

    serializer_class = SponserCreateSerializer

    def create(self, request):
        # username = request.data.get("username")
        # password = request.data.get("password")
        # first_name = request.data.get("firstName")
        # last_name = request.data.get("lastName")
        # email = request.data.get("email")
        new_user = User.objects.create_user(
            username=request.data.get("username"),
            password=request.data.get("password"),
            first_name=request.data.get("firstName"),
            last_name=request.data.get("lastName"),
            email=request.data.get("email"),
            is_active=True,
        )
        new_sponser = Sponser.objects.create(
            user=new_user,
        )
        headers = self.get_success_headers(
            SponserCreateSerializer(new_sponser).data)
        return Response(SponserCreateSerializer(new_sponser).data, headers=headers)


class MyTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
