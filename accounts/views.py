from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
from accounts.serializers import SponseeCreateSerializer, SponserCreateSerializer, ReasonSerializer, SchoolSerializer
from accounts.models import Sponsee, User, School, Reason, Sponser, Sponsee
from accounts.permissions import IsOwnerOrReadOnly
from rest_framework.settings import api_settings


class CreateSponseeView(CreateAPIView):

    serializer_class = SponseeCreateSerializer

    def create(self, request):
        # print(request.data.get("user.username"))
        new_user = User.objects.create_user(
            username=request.data.get("user.username"),
            password=request.data.get("user.password"),
            first_name=request.data.get("user.first_name"),
            last_name=request.data.get("user.last_name"),
            email=request.data.get("user.email"),
            is_active=True,
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
        return Response(SponseeCreateSerializer(new_sponsee).data, headers=headers)


class CreateSponserView(CreateAPIView):

    serializer_class = SponserCreateSerializer

    def create(self, request):
        new_user = User.objects.create_user(
            username=request.data.get("user.username"),
            password=request.data.get("user.password"),
            first_name=request.data.get("user.first_name"),
            last_name=request.data.get("user.last_name"),
            email=request.data.get("user.email"),
            is_active=True,
        )
        new_sponser = Sponser.objects.create(
            user=new_user,
        )
        headers = self.get_success_headers(
            SponserCreateSerializer(new_sponser).data)
        return Response(SponserCreateSerializer(new_sponser).data, headers=headers)


class SponseeReasonView(GenericAPIView):

    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={
            "reason": request.data.get("reason"),
            "student": Sponsee.objects.get(user__username=request.user.username).id
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = Reason.objects.get(
                student__user__username=request.user.username)
        except Reason.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance = Reason.objects.get(
            student__user__username=request.user.username)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = Reason.objects.get(
                student__user__username=request.user.username)
        except Reason.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = Reason.objects.get(
            student__user__username=request.user.username)
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class SponseeSchoolAPIView(GenericAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data={
            "student": Sponsee.objects.get(user__username=request.user.username).id,
            "name": request.data.get("name"),
            "address": request.data.get("address"),
            "academic_level": request.data.get("academic_level"),
            "expected_year_of_completion": request.data.get("expected_year_of_completion"),
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = School.objects.get(
                student__user__username=request.user.username)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance = School.objects.get(
            student__user__username=request.user.username)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = School.objects.get(
                student__user__username=request.user.username)
        except School.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = School.objects.get(
            student__user__username=request.user.username)
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()
