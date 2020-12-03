from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Sponsee, School, Reason, Sponser
from accounts.serializers.userserializers import *
import datetime


class MyCurrentSponseeDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.sponsee

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class SponseeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsee
        fields = ['user', 'address', 'phone',
                  'birth_certificate', 'national_id']


class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    academic_level = serializers.IntegerField(
        required=True, min_value=1, max_value=12)
    expected_year_of_completion = serializers.IntegerField(
        required=True, min_value=datetime.date.today().year+1, max_value=datetime.date.today().year+13)
    student = serializers.HiddenField(
        default=MyCurrentSponseeDefault()
    )

    class Meta:
        model = School
        fields = ["student", "name", "address", "academic_level",
                  "expected_year_of_completion"]


class ReasonSerializer(serializers.ModelSerializer):

    student = serializers.HiddenField(
        default=MyCurrentSponseeDefault()
    )
    reason = serializers.CharField(required=True)

    class Meta:
        model = Reason
        fields = ["reason", "student"]


class SponseeListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    school = SchoolSerializer(read_only=True)
    reason = ReasonSerializer(read_only=True)

    class Meta:
        model = Sponsee
        fields = [
            'phone',
            'birth_certificate',
            'national_id',
            'user',
            "school",
            "reason",
        ]
