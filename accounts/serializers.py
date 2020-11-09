from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models import Sponsee


class SponseeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sponsee
        fields = ['id', 'user', 'address', 'phone',
                  'birth_certificate', 'national_id']


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
