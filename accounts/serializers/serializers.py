from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import Sponsee, School, Reason, Sponser
from accounts.serializers.userserializers import UserSerializer, UserRetrieveSerializer
from accounts.utils import check_user_type


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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_type = check_user_type(self.user)
        data['user'] = user_type
        return data
        # user_type = None
        # try:
        #     the_user = self.user.sponsee
        #     user_type = "sponsee"
        # except User.sponsee.RelatedObjectDoesNotExist:
        #     the_user = None
        # if(the_user == None):
        #     try:
        #         the_user = self.user.sponser
        #         user_type = "sponser"
        #     except User.sponser.RelatedObjectDoesNotExist:
        #         user_type = "staff"
        #         the_user = None
        # data['user'] = user_type
        # return data
