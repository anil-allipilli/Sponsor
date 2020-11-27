from accounts.models import Sponsee, User, School, Reason, Sponser
from rest_framework import viewsets
from accounts.serializers import (
    SponseeCreateSerializer,
    UserSerializer,
    SchoolSerializer,
    ReasonSerializer,
    SponserSerializer,
    SponseeListSerializer
)
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from accounts.permissions import IsOwnerOrSponsorStaffReadOnly, SponseeOrStaffReadOnly, MyPermissionMixin
from rest_framework.generics import GenericAPIView, get_object_or_404
from accounts.utils import check_user_type
from rest_framework.decorators import action
from django.http import Http404
# from django.shortcuts import get_object_or_404 as _get_object_or_404


class GetObjectMixin:
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(
            queryset, **{"student": self.request.user.sponsee})
        self.check_object_permissions(self.request, obj)
        return obj


class SponserViewSet(viewsets.ModelViewSet):

    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer


class SponseeListViewSet(MyPermissionMixin, viewsets.ModelViewSet):
    queryset = Sponsee.objects.all()
    serializer_class = SponseeListSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(
            queryset, **{"user": self.request.user})
        self.check_object_permissions(self.request, obj)
        return obj


class SchoolViewSet(GetObjectMixin, MyPermissionMixin, viewsets.ModelViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ReasonViewSet(GetObjectMixin, MyPermissionMixin, viewsets.ModelViewSet):

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
