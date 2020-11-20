from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

from accounts.viewsets import (
    UserViewSet,
    SchoolViewSet,

    SponserViewSet,
    SponseeListViewSet
)
from accounts.views import CreateSponseeView, CreateSponserView, SponseeReasonView, SponseeSchoolAPIView, SponseeAPIView, MyTokenObtainPairView

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("schools", SchoolViewSet, basename="schools")
# router.register("reasons", ReasonViewSet, basename="reasons")
router.register("sponsers", SponserViewSet, basename="sponsers")
router.register("sponsees", SponseeListViewSet, basename="sponsees")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/createsponsee/',
         CreateSponseeView.as_view()),
    path('api/createsponser/',
         CreateSponserView.as_view()),
    path('reason/',
         SponseeReasonView.as_view()),
    path('school/',
         SponseeSchoolAPIView.as_view()),
    path('sponsee-detail/',
         SponseeAPIView.as_view()),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
