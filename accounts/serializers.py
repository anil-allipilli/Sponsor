from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response

from accounts.models import Sponsee, School, Reason, Sponser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'password',
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

    def create(self, validated_data):
        # print(validated_data)
        return Sponsee(**validated_data)


class SponserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponser
        fields = "__all__"


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'


class ReasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reason
        fields = '__all__'
