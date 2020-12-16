
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status, mixins
from accounts.serializers import (
    SponserSerializer,
    MyTokenObtainPairSerializer,
    UserSerializer
)
from accounts.models import Sponsee, User, School, Reason, Sponser, Sponsee

from rest_framework.settings import api_settings
from rest_framework_simplejwt import views as jwt_views
from rest_framework.decorators import api_view
from accounts.utils import check_user_type
from accounts.tasks import send_staff_email_task


class CreateSponserView(CreateAPIView):

    def create(self, request):
        serializer = UserSerializer(data={
            "username": request.data.get("username"),
            "password": request.data.get("password"),
            "first_name": request.data.get("firstName"),
            "last_name": request.data.get("lastName"),
            "email": request.data.get("email"),
        })
        serializer.is_valid(raise_exception=True)
        new_user = serializer.save()
        new_sponser = Sponser.objects.create(user=new_user)
        headers = self.get_success_headers(
            SponserSerializer(new_sponser).data)
        return Response(SponserSerializer(new_sponser).data, headers=headers)


class MyTokenObtainPairView(jwt_views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def add_sponsorship(request, username):
    if(check_user_type(request.user) == "sponser"):
        sponser = Sponser.objects.get(user=request.user)
        sponsee = Sponsee.objects.get(user__username=username)
        sponser.mysponsees.add(sponsee)
        send_staff_email_task.delay(sponser, sponsee)
        return Response(SponserSerializer(sponser, context={'request': request}).data)
    return Response(status=HTTP_404_NOT_FOUND)
