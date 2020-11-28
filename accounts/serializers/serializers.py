from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import Sponser
from accounts.serializers.userserializers import UserSerializer
from accounts.utils import check_user_type


class SponserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponser
        fields = ["user"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_type = check_user_type(self.user)
        data['user'] = user_type
        return data
