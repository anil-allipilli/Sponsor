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


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ["name", "address", ]


class ReasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reason
        fields = ["reason"]


class SponserSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()

    class Meta:
        model = Sponser
        fields = ["user"]


class SponseeListSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()
    reason = ReasonSerializer()

    class Meta:
        model = Sponsee
        fields = ['user', 'phone', "school", "reason",
                  'birth_certificate', 'national_id']
