from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from accounts.serializers import SponseeCreateSerializer
from accounts.models import Sponsee, User, School, Reason, Sponser


class CreateSponseeView(CreateAPIView):

    serializer_class = SponseeCreateSerializer

    def create(self, request):
        new_user = User.objects.create(
            username=request.data.get("user.username"),
            password=request.data.get("user.password"),
            first_name=request.data.get("user.first_name"),
            last_name=request.data.get("user.last_name"),
            email=request.data.get("user.email"),
        )
        new_sponsee = Sponsee.objects.create(
            user=new_user,
            address=request.data.get("address"),
            phone=request.data.get("phone"),
            birth_certificate=request.data.get("birth_certificate"),
            national_id=request.data.get("national_id"),
        )
        headers = self.get_success_headers(
            SponseeCreateSerializer(new_sponsee).data)
        # print(SponseeSerializer(new_sponsee).data)
        return Response(SponseeCreateSerializer(new_sponsee).data, headers=headers)
