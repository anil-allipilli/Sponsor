from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models import Sponsee, School, Reason, Sponser


class SponseeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsee
        fields = ['id', 'user', 'address', 'phone',
                  'birth_certificate', 'national_id']


class SponserSerializer(serializers.ModelSerializer):

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
