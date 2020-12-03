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
from accounts.permissions import IsOwnerOrSponsorStaffReadOnly, SponseeOrStaffReadOnly, MyPermissionMixin, UserProfilePermission
from rest_framework.generics import GenericAPIView, get_object_or_404
from accounts.utils import check_user_type
from rest_framework.decorators import action
from django.http import Http404
# from django.shortcuts import get_object_or_404 as _get_object_or_404


class GetObjectMixin:
    def get_object(self):
        print("hello")
        if(check_user_type(self.request.user) == "sponsee"):
            print("hello")
            queryset = self.filter_queryset(self.get_queryset())
            obj = get_object_or_404(
                queryset, **{"student": self.request.user.sponsee})
            self.check_object_permissions(self.request, obj)
            return obj
        else:
            return super().get_object()


class SponserViewSet(viewsets.ModelViewSet):

    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer


class SponseeListViewSet(MyPermissionMixin, viewsets.ModelViewSet):
    queryset = Sponsee.objects.all()
    serializer_class = SponseeListSerializer

    def get_object(self):
        if(check_user_type(self.request.user) == "sponsee"):
            queryset = self.filter_queryset(self.get_queryset())
            obj = get_object_or_404(
                queryset, **{"user": self.request.user})
            self.check_object_permissions(self.request, obj)
            return obj
        else:
            return super().get_object()


class SchoolViewSet(GetObjectMixin, MyPermissionMixin, viewsets.ModelViewSet):

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ReasonViewSet(GetObjectMixin, MyPermissionMixin, viewsets.ModelViewSet):
    # class ReasonViewSet(viewsets.ModelViewSet):

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class SponseeReasonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    viewset for sponsor to view reason of sponsee in detail page searched by username
    """
    queryset = Reason.objects.all()
    permission_classes = [IsAuthenticated & SponseeOrStaffReadOnly]
    serializer_class = ReasonSerializer
    lookup_field = "username"

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        username = self.kwargs[self.lookup_field]
        try:
            obj = queryset.get(
                student__user__username=username)
        except Reason.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & UserProfilePermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated & SponseeOrStaffReadOnly]
        elif (self.action in ['retrieve', 'update', 'partial_update', 'create']):
            print("hrllp")
            permission_classes = [IsAuthenticated &
                                  UserProfilePermission]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
