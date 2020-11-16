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

from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsOwnerOrReadOnly
from rest_framework.generics import GenericAPIView


class SponserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Sponser.objects.all()
    serializer_class = SponserSerializer


class SponseeListViewSet(viewsets.ReadOnlyModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Sponsee.objects.all()
    serializer_class = SponseeListSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


# class ReasonViewSet(GenericAPIView):
#     permission_classes = [IsOwnerOrReadOnly]

#     queryset = Reason.objects.all()
#     serializer_class = ReasonSerializer

#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(
#             instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to
#             # forcibly invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         return Response(serializer.data)

#     def perform_update(self, serializer):
#         serializer.save()

#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
