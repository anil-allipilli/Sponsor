"""sponsor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.viewsets import UserViewSet, SchoolViewSet, ReasonViewSet, SponserViewSet
from accounts.views import CreateSponseeView

router = DefaultRouter()
# router.register("sponsees", SponseeViewSet, basename="accounts")
router.register("users", UserViewSet, basename="users")
router.register("schools", SchoolViewSet, basename="schools")
router.register("reasons", ReasonViewSet, basename="reasons")
router.register("sponsers", SponserViewSet, basename="sponsers")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/createsponser',
         CreateSponseeView.as_view()),
    # path('api/createsponser',
    #      SponseeCreateViewSet.as_view({'post': 'create'})),
    path('', include(router.urls)),
]
