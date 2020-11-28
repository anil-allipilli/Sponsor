from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
from accounts.serializers import (
    SponseeCreateSerializer,
    SponseeListSerializer,
    UserSerializer
)
from rest_framework.settings import api_settings


class CreateSponseeView(CreateAPIView):

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

        sponsee_serializer = SponseeCreateSerializer(data={
            "user": new_user.pk,
            "address": request.data.get("address"),
            "phone": request.data.get("phone"),
            "birth_certificate": request.data.get("birthCertificate"),
            "national_id": request.data.get("nationalId"),
        })
        sponsee_serializer.is_valid(raise_exception=True)
        new_sponsee = sponsee_serializer.save()
        headers = self.get_success_headers(
            SponseeCreateSerializer(new_sponsee).data)
        return Response(SponseeListSerializer(new_sponsee).data, headers=headers)
