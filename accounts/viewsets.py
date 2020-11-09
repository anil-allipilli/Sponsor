from accounts.models import Sponsee, User
from rest_framework import viewsets
from accounts.serializers import SponseeSerializer, UserSerializer


class SponseeViewSet(viewsets.ModelViewSet):

    queryset = Sponsee.objects.all()
    serializer_class = SponseeSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
