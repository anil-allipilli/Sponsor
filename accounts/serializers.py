from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response

from accounts.models import Sponsee, School, Reason, Sponser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'password',
            'username',
            'first_name',
            'last_name',
            "email"
        ]


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [

            'username',
            'first_name',
            'last_name',
            "email"
        ]


class SponseeCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponsee
        fields = ['id', 'user', 'address', 'phone',
                  'birth_certificate', 'national_id']


class SponseeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsee
        fields = ['user', 'phone',
                  'birth_certificate', 'national_id']


class SponserCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponser
        fields = ['user']


# class SponserListSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Sponser
#         fields = ['user', 'phone',
#                   'birth_certificate', 'national_id']


class SponserSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()

    class Meta:
        model = Sponser
        fields = ["user"]


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'


class ReasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reason
        fields = '__all__'
