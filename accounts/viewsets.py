from accounts.models import Sponsee, User, School, Reason, Sponser
from rest_framework import viewsets
from accounts.serializers import (
    SponseeSerializer,
    UserSerializer,
    SchoolSerializer,
    ReasonSerializer,
    SponserSerializer
)


class SponseeViewSet(viewsets.ModelViewSet):

    queryset = Sponsee.objects.all()
    serializer_class = SponseeSerializer


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
