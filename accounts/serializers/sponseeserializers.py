from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Sponsee, School, Reason, Sponser
from accounts.serializers.userserializers import *


class MyCurrentSponseeDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.sponsee

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class SponseeCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponsee
        fields = ['id', 'user', 'address', 'phone',
                  'birth_certificate', 'national_id']


# class SponseeListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Sponsee
#         fields = ['user', 'phone',
#                   'birth_certificate', 'national_id']


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ["name", "address", "academic_level",
                  "expected_year_of_completion"]


class ReasonSerializer(serializers.ModelSerializer):

    student = serializers.HiddenField(
        default=MyCurrentSponseeDefault()
    )

    class Meta:
        model = Reason
        fields = ["reason", "student"]


class SponseeListSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    reason = ReasonSerializer()
    user = UserRetrieveSerializer()

    class Meta:
        model = Sponsee
        fields = ['user', 'phone', "school", "reason",
                  'birth_certificate', 'national_id']
