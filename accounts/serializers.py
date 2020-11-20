from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
        fields = ["student", "name", "address", "academic_level",
                  "expected_year_of_completion"]


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
    user = UserRetrieveSerializer()

    class Meta:
        model = Sponsee
        fields = ['user', 'phone', "school", "reason",
                  'birth_certificate', 'national_id']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_type = None
        try:
            the_user = self.user.sponsee
            user_type = "sponsee"
        except User.sponsee.RelatedObjectDoesNotExist:
            the_user = None
        if(the_user == None):
            try:
                the_user = self.user.sponser
                user_type = "sponser"
            except User.sponser.RelatedObjectDoesNotExist:
                user_type = "staff"
                the_user = None
        data['user'] = user_type
        return data
