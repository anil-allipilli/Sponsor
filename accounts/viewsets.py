from accounts.models import Sponsee, User, School, Reason, Sponser
from rest_framework import viewsets
from accounts.serializers import (
    SponseeCreateSerializer,
    UserSerializer,
    SchoolSerializer,
    ReasonSerializer,
    SponserSerializer
)
from rest_framework.response import Response
from rest_framework import generics, mixins, views


# class SponseeCreateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet, ):

#     queryset = Sponsee.objects.all()
#     serializer_class = SponseeCreateSerializer

#     def create(self, request):
#         new_user = User.objects.create(
#             username=request.data.get("user.username"),
#             password=request.data.get("user.password"),
#             first_name=request.data.get("user.first_name"),
#             last_name=request.data.get("user.last_name"),
#             email=request.data.get("user.email"),
#         )
#         new_sponsee = Sponsee.objects.create(
#             user=new_user,
#             address=request.data.get("address"),
#             phone=request.data.get("phone"),
#             birth_certificate=request.data.get("birth_certificate"),
#             national_id=request.data.get("national_id"),
#         )
#         headers = self.get_success_headers(SponseeSerializer(new_sponsee).data)
#         print(SponseeSerializer(new_sponsee).data)
#         return Response(SponseeSerializer(new_sponsee).data, headers=headers)


class SponserViewSet(viewsets.ModelViewSet):

    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer


class SchoolViewSet(viewsets.ModelViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ReasonViewSet(viewsets.ModelViewSet):

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
